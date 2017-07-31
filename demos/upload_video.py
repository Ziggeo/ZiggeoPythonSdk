import sys

from Ziggeo import Ziggeo
import json
if(len(sys.argv) < 4):
	print ("Error\n")
	print ("Usage: $>python upload_video.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_FILE\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_file = sys.argv[3]

ziggeo = Ziggeo(api_token, private_key)
ziggeo.videos().create(file = video_file)
