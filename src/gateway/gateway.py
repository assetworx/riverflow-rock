#   _____  _                 __ _               
#  |  __ \(_)               / _| |              
#  | |__) |___   _____ _ __| |_| | _____      __
#  |  _  /| \ \ / / _ \ '__|  _| |/ _ \ \ /\ / /
#  | | \ \| |\ V /  __/ |  | | | | (_) \ V  V / 
#  |_|  \_\_| \_/ \___|_|  |_| |_|\___/ \_/\_/  
#
#  Riverflow API gateway definitions.

import sys
sys.path.append("..")
from frameworks.keras import KerasBasedModel
frameworks_supported = ['keras']

# Check if Riverflow supports framework supplied by env.
def supports_framework(framework):
  return framework in frameworks_supported

# Load a model
def load_model(framework):
  if framework == 'keras':
    return KerasBasedModel()