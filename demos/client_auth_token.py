import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print "Error\n"
	print "Usage: $>python client_auth_token.py YOUR_API_TOKEN YOUR_PRIVATE_KEY ENCRYPTION_KEY \n"
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
encryption_key = sys.argv[3]

ziggeo = Ziggeo(api_token, private_key, encryption_key)

arguments={}
arguments["session_limit"] = 10
arguments["grants"] = '{"read": "all"}'

print ziggeo.authtokens().create(arguments)