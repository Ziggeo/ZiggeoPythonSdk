import os, sys
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print("Error\n")
	print("Usage: $>python _streams_download_video.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]

ziggeo = Ziggeo(app_token, private_key)

video_data = ziggeo.videos().get(video_token)

stream_token = video_data["default_stream"]["token"]
file_name = video_token + "_" + stream_token + '.' + video_data["default_stream"]["video_type"]

# We are using "wb" for write binary. To prevent windows from using write as non binary
file = open('assets/' + file_name, "wb")

downloaded_file = ziggeo.streams().download_video(video_token, stream_token)

file.write(downloaded_file)
file.close()