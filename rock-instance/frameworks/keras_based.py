from keras.models import load_model
import numpy as np
import tensorflow as tf
import json

#
#  _______  ___   __   __  _______ 
# |   _   ||   | |  |_|  ||       |
# |  |_|  ||   | |       ||    ___|
# |       ||   | |       ||   |___ 
# |       ||   | |       ||    ___|
# |   _   ||   | | ||_|| ||   |___ 
# |__| |__||___| |_|   |_||_______|
#
# Keras based model class
class KerasBasedModel:

  # Constructor
  def __init__(self):
    self.session = tf.Session()
    self.graph = tf.get_default_graph()
    # Avoid hanging of graph and session
    with self.graph.as_default():
      with self.session.as_default():
        print('Model was initialized.')        
  
  #
  # @def load_model
  # Load the model 
  #
  # @param <KerasBasedModel> self
  # @param <String> filepath Location of the model
  # @param <Object> custom_objects Custom objects to Keras
  # @param <Boolean> to_compile Whether to compile the model after loading.
  # @return <keras.models.Model> Model instance
  # @raise Exception invalid-path
  #
  def load_model(self, filepath, custom_objects = None, to_compile = True):
    if filepath is None or type(filepath) is not str:
      raise Exception('Invalid path to model.')
    with self.graph.as_default():
      with self.session.as_default():
        self.model = load_model(filepath, custom_objects, to_compile)
        return self.model

  #
  # @def predict
  # Generate a prediction
  #
  # @docs https://keras.io/models/sequential/#predict
  # @docs https://keras.io/models/model/#predict 
  #
  # @param <KerasBasedModel> self
  # @param <np.array> x Data for prediction.
  # @param <Integer> batch_size
  # @param <Boolean> verbose
  # @param <Integer> steps
  # @param <List<keras.callbacks.Callback>> callbacks
  # @return <np.array> predictions
  # @raise Exception no-model-exception
  #
  def predict(self, x, batch_size = None, verbose = 0, steps = None, callbacks = None):
    if self.model is None:
      raise Exception('No model loaded yet.')
    with self.graph.as_default():
      with self.session.as_default():
        # Todo: support beyond data
        predictions = self.model.predict(x)
        return json.dumps(predictions.tolist())