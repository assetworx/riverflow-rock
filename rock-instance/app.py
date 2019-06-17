#!/usr/bin/env python3
from flask import Flask
from flask import jsonify

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

# Basic route
@app.route('/')
def home_route():
  response_dict = {
    'success': True,
    'status': 'Riverflow Rock instance seems to be working!'
  }
  return jsonify(response_dict)

# Run app
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')