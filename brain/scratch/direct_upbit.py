import requests
import time
import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import os
from dotenv import load_dotenv

load_dotenv()

access_key = os.getenv('UPBIT_ACCESS_KEY')
secret_key = os.getenv('UPBIT_SECRET_KEY')
server_url = "https://api.upbit.com"

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(server_url + "/v1/accounts", headers=headers)
print(f"Status Code: {res.status_code}")
print(f"Headers: {res.headers}")
print(f"Response: {res.text}")
