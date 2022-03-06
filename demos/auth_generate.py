import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print("Error\n")
	print("Usage: $>python auth_generate.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY ENCRYPTION_KEY \n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
encryption_key = sys.argv[3]

ziggeo = Ziggeo(app_token, private_key, encryption_key)

arguments = {}
arguments["session_limit"] = 10
arguments["grants"] = '{"read": "all"}'

print(ziggeo.auth().generate(arguments))