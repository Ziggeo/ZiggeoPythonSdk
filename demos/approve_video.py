import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print ("Error\n")
	print ("Usage: $>python approve_video.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]

ziggeo = Ziggeo(api_token, private_key)

print (ziggeo.videos().update(video_token, {"approved": True}))
