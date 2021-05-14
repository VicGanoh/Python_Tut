# This code will show you how to call the Computer Vision API from Python
# You can find documentation on the Computer Vision Analyze Image method here
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Use the requests library to simplify making a REST API call from Python
import requests

# We will need the json library to read the data passed back 
# by the web service
import json 

# You need to update the SUBSCRIPTION_KEY to 
# they key for your Computer Vision Service
SUBSCRIPTION_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';

