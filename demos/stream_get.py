import sys

from Ziggeo import Ziggeo
import json
if(len(sys.argv) < 5):
	print ("Error\n")
	print ("Usage: $>python stream_get.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN STREAM_TOKEN PUSH_SERVICE_TOKEN\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]
stream_token = sys.argv[4]

ziggeo = Ziggeo(api_token, private_key)

print (ziggeo.streams().get(video_token, stream_token))