import json
import requests

response = requests.get('https://codingninjas.in/api/v3/courses')
python_file = json.loads(response.text)
print(python_file)
