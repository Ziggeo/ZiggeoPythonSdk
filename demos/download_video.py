import sys

from Ziggeo import Ziggeo
import json
if(len(sys.argv) < 4):
	print "Error\n"
	print "Usage: $>python download_video.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN\n"
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]

ziggeo = Ziggeo(api_token, private_key)
video_data = ziggeo.videos().get(video_token)
file_name = video_token+'.'+video_data["original_stream"]["video_type"]

file = open(file_name, "w")
downloaded_file = ziggeo.videos().download_video(video_token)
file.write(downloaded_file)
file.close()