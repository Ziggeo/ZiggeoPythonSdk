import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print("Error\n")
	print("Usage: $>python effectprofiles_index.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]

index_arguments = {}
index_arguments["limit"] = 50

ziggeo = Ziggeo(app_token, private_key)

print(ziggeo.effectProfiles().index(index_arguments))