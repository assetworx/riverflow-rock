#   _____  _                 __ _               
#  |  __ \(_)               / _| |              
#  | |__) |___   _____ _ __| |_| | _____      __
#  |  _  /| \ \ / / _ \ '__|  _| |/ _ \ \ /\ / /
#  | | \ \| |\ V /  __/ |  | | | | (_) \ V  V / 
#  |_|  \_\_| \_/ \___|_|  |_| |_|\___/ \_/\_/  
#
#  Support for Keras based models.

from keras.models import load_model
import numpy as numpy
import tensorflow as tf
import os.path

class KerasBasedModel:

  # Constructor
  # Loads Tensorflow session and graph
  def __init__(self):
    self.session = tf.Session()
    self.graph = tf.get_default_graph()
    with self.graph.as_default():
      with self.session.as_default():
        print('Loading model')
        self.load_model()
        print('Model initialized successfully.')

  # Load a Keras model
  def load_model(self, custom_objects = None, to_compile = True):
    filepath = '/app/model-files/model'
    if not os.path.exists(filepath):
      raise Exception(f'Model could not be found at path {filepath}')
    # Load model
    with self.graph.as_default():
      with self.session.as_default():
        self.model = load_model(filepath, custom_objects, to_compile)
        return self.model

  # Generate a prediction
  def predict(self, x):
    if self.model is None:
      raise Exception('No model loaded yet.')
    with self.graph.as_default():
      with self.session.as_default():
        # Todo: support beyond data
        predictions = self.model.predict(x).tolist()
        return predictions