import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
    print ("Error\n")
    print ("Usage: $>python application_update.py YOUR_API_TOKEN YOUR_PRIVATE_KEY\n")
    sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
ziggeo = Ziggeo(api_token, private_key)
application_args = {}
application_args['name'] = "new name" # change the application's name
application_args['auth_token_required_for_create'] = True # set option to require auth token when creating new video.
ziggeo.application().update(application_args)
