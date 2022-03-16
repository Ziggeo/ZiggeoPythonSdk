import os, sys
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 5):
	print("Error\n")
	print("Usage: $>python streams_delete.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN STREAM_TOKEN \n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]
stream_token = sys.argv[4]

ziggeo = Ziggeo(app_token, private_key)

ziggeo.streams().delete(video_token, stream_token)