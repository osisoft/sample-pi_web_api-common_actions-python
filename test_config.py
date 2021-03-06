import json

# Try to open the configuration file
try:
    with open(
        'test_config.json',
        'r',
    ) as f:
        config = json.load(f)
except Exception as error:
    print(f'Error: {str(error)}')
    print(f'Could not open/read file: test_config.json')
    exit()

PIWEBAPI_URL = config.get('Resource')
AF_SERVER_NAME = config.get('AssetServerName')
PI_SERVER_NAME = config.get('DataServerName')
USER_NAME = config.get('Username')
USER_PASSWORD = config.get('Password')
AUTH_TYPE = config.get('AuthType', 'kerberos')
VERIFY_SSL = config.get('VerifySSL', True)

