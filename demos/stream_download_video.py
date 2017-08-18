import sys

from Ziggeo import Ziggeo
import json
if(len(sys.argv) < 5):
	print ("Error\n")
	print ("Usage: $>python stream_download_video.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN STREAM_TOKEN PUSH_SERVICE_TOKEN\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]
stream_token = sys.argv[4]

ziggeo = Ziggeo(api_token, private_key)

stream_info = ziggeo.streams().get(video_token, stream_token)

file_name = video_token + "_" + stream_token + "." + stream_info["video_type"]
file = open('assets/' + file_name, "wb")
downloaded_file = ziggeo.streams().download_video(video_token, stream_token)
file.write(downloaded_file)
file.close()