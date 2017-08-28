import sys

from Ziggeo import Ziggeo
import json
if(len(sys.argv) < 5):
	print ("Error\n")
	print ("Usage: $>python stream_delete.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN stream_token \n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]
stream_token = sys.argv[4]

ziggeo = Ziggeo(api_token, private_key)

ziggeo.streams().delete(video_token, stream_token)
