import requests
import os
import dotenv
import facebook

dotenv.load_dotenv()

token = os.getenv("TOKEN_FACEBOOK")
response = requests.get(f"https://graph.facebook.com/me?access_token={token}")

if response.status_code == 200:
    print("✓ Token válido:", response.json())
else:
    print("✗ Error:", response.text)

