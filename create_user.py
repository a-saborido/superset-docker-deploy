import requests
import json

############################################################# GENERATE ACCESS TOKEN #############################################################

# URL of the Superset login endpoint
url_login = "http://localhost:8088/api/v1/security/login"

# Headers for the request
headers_login = {
    'Content-Type': 'application/json'
}

# Request body with login credentials
request_body_login = {
    "username": "admin",
    "password": "admin",
    "provider": "db",
    "refresh": True
}

# Sending the POST request
response = requests.post(url_login, headers=headers_login, data=json.dumps(request_body_login))

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

############################################################# CREATION OF NEW USER #############################################################

# Replace with your actual tokens
ACCESS_TOKEN = access_token

# URL of the Superset user creation endpoint
url = "http://localhost:8088/api/v1/security/users/"

# Headers for the request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {ACCESS_TOKEN}',
}

# Request body with user details
request_body = {
    "active": True,
    "username": "alberto_alpha",
    "first_name": "Alberto",
    "last_name": "Saborido",
    "email": "alberto_alpha@superset.com",
    "password": "1234",
    "roles": [3],
    
}

# Sending the POST request
response = requests.post(url, headers=headers, data=json.dumps(request_body))

# Checking the response
if response.status_code == 201:
    print("User created successfully")
else:
    print("Failed to create user")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
