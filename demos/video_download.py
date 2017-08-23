import sys

from Ziggeo import Ziggeo
import json
if(len(sys.argv) < 4):
	print ("Error\n")
	print ("Usage: $>python video_download.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]

ziggeo = Ziggeo(api_token, private_key)
video_data = ziggeo.videos().get(video_token)
stream_token = video_data["default_stream"]["token"]
file_name = video_token+"_"+stream_token+'.'+video_data["default_stream"]["video_type"]

# We are using "wb" for write binary. To prevent windows from using write as non binary
file = open('assets/' + file_name, "wb")
downloaded_file = ziggeo.streams().download_video(video_token, stream_token)
file.write(downloaded_file)
file.close()
