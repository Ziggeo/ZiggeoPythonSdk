import sys

from Ziggeo import Ziggeo
import json
if(len(sys.argv) < 5):
	print ("Error\n")
	print ("Usage: $>python push_video.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN PUSH_SERVICE_TOKEN\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]
push_service_token = sys.argv[4]

ziggeo = Ziggeo(api_token, private_key)
arguments = {}
arguments['pushservicetoken'] = push_service_token
ziggeo.videos().push_to_service(video_token, arguments)
