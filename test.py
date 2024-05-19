from cryptography import fernet
import os

########################ENCRYPT API KEYS##########################
#key = os.getenv('API_ENCRYPTION_KEY')
#if key is None:
#    raise ValueError("No API_ENCRYPTION_KEY found in environment variables")
#
#encrypt = fernet.Fernet(key)
#
#vt = b''
#hybrid = b''
#
#evt = encrypt.encrypt(vt)
#ehybrid = encrypt.encrypt(hybrid)
#
#with open(r'Spyware_Manager\api_keys.txt', 'wb') as file:
#    file.write(evt + b'\n' + ehybrid)
########################ENCRYPT API KEYS##########################

