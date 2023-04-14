import requests

# Request headers
headers = {
    'Authorization': 'Bearer YOUR_TWITCH_OAUTH_TOKEN',
    'Client-Id': 'YOUR_TWITCH_CLIENT-ID',
}

# Request parameters
params = {
    'login': 'LOGIN_STREAMER', # replace with username
}

# Send request
response = requests.get('https://api.twitch.tv/helix/users', params=params, headers=headers)

# Process response
if response.status_code == 200:
    user_id = response.json()['data'][0]['id']
    print(f"USERID of USERNAME: {user_id}")
else:
    print(f"Error occurred: {response.text}")
