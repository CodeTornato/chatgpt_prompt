import requests
import json

# Define the endpoint URL
url = "https://api.openai.com/v1/images/generations"

# Set the request headers

headers = {
    "Content-Type": "application/json",
    "Authorization": "YOUR_API_KEY"
} # paste your api key for the authrization

# Define the request payload
payload = {
    "prompt": "Obi-Wan Kenobi fighting with lightsaber with Darth Vadar in the dead star,be realistic,like in the movie",
    "n": 2,
    "size": "1024x1024"
}

# Send the API request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Get the API response
api_response = response.json()

# Extract the image generation results
# Depending on the API response structure, you may need to adjust this
# image_results = api_response["output"]["images"]
print(api_response)
# Process the image results as needed
# ...
