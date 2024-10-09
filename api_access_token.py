import requests
import json

# URL of the Superset login endpoint
url = "http://localhost:8088/api/v1/security/login"

# Headers for the request
headers = {
    'Content-Type': 'application/json'
}

# Request body with login credentials
request_body = {
    "username": "admin",
    "password": "admin",
    "provider": "db",
    "refresh": True,
}

# Sending the POST request
response = requests.post(url, headers=headers, data=json.dumps(request_body))

# Checking the response
if response.status_code == 200:
    print("Login successful")
    # Parsing the JSON response
    data = response.json()
    access_token = data.get('access_token')
    print("Access Token:", access_token)
else:
    print("Login failed")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
