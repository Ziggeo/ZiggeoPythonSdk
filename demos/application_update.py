import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print("Error\n")
	print("Usage: $>python application_update.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]

ziggeo = Ziggeo(app_token, private_key)

application_args = {}
application_args['name'] = "new name" # change the application's name
application_args['auth_token_required_for_create'] = True # set option to require auth token when creating new video.

ziggeo.application().update(application_args)