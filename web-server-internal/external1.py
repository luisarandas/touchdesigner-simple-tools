

# luis arandas 23-07-2022
# external python code that reaches touchdesigner

import requests

url = 'http://127.0.0.1:9980' # or machine ip
data = {'special_parameter_value': 'helloooooooooooooooooooooo external'}

r = requests.post(url, json=data)