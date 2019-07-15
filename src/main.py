#   _____  _                 __ _               
#  |  __ \(_)               / _| |              
#  | |__) |___   _____ _ __| |_| | _____      __
#  |  _  /| \ \ / / _ \ '__|  _| |/ _ \ \ /\ / /
#  | | \ \| |\ V /  __/ |  | | | | (_) \ V  V / 
#  |_|  \_\_| \_/ \___|_|  |_| |_|\___/ \_/\_/  
#
#  Riverflow FastAPI entry point.

from fastapi import FastAPI, Body
from gateway import gateway
import os
import ast

# Pick up ML framework from env, default to Keras
ml_framework = os.environ.get('ML_FRAMEWORK', 'keras')
if not gateway.supports_framework(ml_framework):
  raise Exception(f'Framework {ml_framework} is not supported.')

# Load model
model = gateway.load_model(ml_framework)

# Define API
app = FastAPI()

# Root entrypoint
@app.get("/")
def root_entrypoint():
    return {
      "status": "Container seems to be working properly."
    }

# Generate prediction
@app.post('/predict')
def generate_prediction(
  body = Body(None, title='POST body.')
):
  try:
    data = body['data']
    if data is None:
      raise Exception('Missing input data.')
    else:
      predictions = model.predict(data)
      return {
        "predictions": predictions
      }
  except Exception as e:
    return {
      "error": str(e)
    }