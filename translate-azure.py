import os
import requests, uuid, json
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv()

key = os.getenv("KEY")
endpoint = os.getenv("ENDPOINT")
location = os.getenv("LOCATION")

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['fr', 'de', 'pt'],  # Changed to translate to French, German, and portuguese
}

headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4()),
}

# Changed text to a more meaningful example
body = [{
    'text': 'Translation is not just about words, it’s about conveying the true meaning across languages!'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

# Print the translated result in a readable format
print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))