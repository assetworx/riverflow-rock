from frameworks.keras_based import *

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
class Framework:

  # @def load
  # Load framework class
  #
  # @param <String> which_framework
  # @return <frameworks> framework
  # @raise Exception non-existing
  def load(self, which_framework):
    if which_framework == 'keras':
      return KerasBasedModel()
    else:
      raise Exception(f'Framework {which_framework} not supported.')