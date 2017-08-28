import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print ("Error\n")
	print ("Usage: $>python authtoken_update.py YOUR_API_TOKEN YOUR_PRIVATE_KEY AUTHTOKEN\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
auth_token = sys.argv[3]

arguments={}
arguments["session_limit"] = 1
arguments["grants"] = '{"write": "all"}'
ziggeo = Ziggeo(api_token, private_key)

print (ziggeo.authtokens().update(auth_token, arguments))
