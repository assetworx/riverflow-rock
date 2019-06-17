#!/usr/bin/env python3
from flask import Flask, jsonify, request
import yaml
from framework import Framework
import ast

#
#  _______  ___   __   __  _______ 
# |   _   ||   | |  |_|  ||       |
# |  |_|  ||   | |       ||    ___|
# |       ||   | |       ||   |___ 
# |       ||   | |       ||    ___|
# |   _   ||   | | ||_|| ||   |___ 
# |__| |__||___| |_|   |_||_______|
#
# Rock instance

# Create app
app = Flask(__name__)

# Load configuration file
config = yaml.load(open('./config.yml', 'r'), Loader=yaml.Loader)

# Load framework and model
fwk = Framework().load(config['which_framework'])
model = fwk.load_model('./model')

# Basic route
@app.route('/')
def home_route():
  response_dict = {
    'success': True,
    'status': 'Riverflow Rock instance seems to be working!'
  }
  return jsonify(response_dict)

# Predict route
@app.route('/predict')
def predict():
  try:
    # Retrieve data
    data = request.args.get('data')
    if data is None:
      raise Exception('Missing input data.')
    # Retrieve prediction
    data = ast.literal_eval(data)
    predictions = model.predict(data)
    response_dict = {
      'success': True,
      'predictions': predictions
    }
  except Exception as e:
    response_dict = {
      'success': False,
      'error': str(e)
    }
  # Return response
  return jsonify(response_dict)

# Run app
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')