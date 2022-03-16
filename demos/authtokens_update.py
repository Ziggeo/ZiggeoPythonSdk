import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print("Error\n")
	print("Usage: $>python authtokens_update.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY AUTHTOKEN\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
auth_token = sys.argv[3]

arguments = {}
arguments["session_limit"] = 1
arguments["grants"] = '{"write": "all"}'

ziggeo = Ziggeo(app_token, private_key)

print(ziggeo.authtokens().update(auth_token, arguments))