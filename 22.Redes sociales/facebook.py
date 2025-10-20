import requests
import os
import dotenv
import facebook



def validarToken(token):
    try:
            response = requests.get(f"https://graph.facebook.com/me?access_token={token}")
            print("Token valido, OK",response.status_code)
    
    except requests.exceptions.HTTPError:
            print("Error al obtener API facebook. Token invalido")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")

dotenv.load_dotenv()

token = os.getenv("TOKEN_FACEBOOK")
validarToken(token)

