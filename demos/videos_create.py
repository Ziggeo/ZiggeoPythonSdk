import os, sys
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print("Error\n")
	print("Usage: $>python videos_create.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY VIDEO_FILE\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
video_file = sys.argv[3]

ziggeo = Ziggeo(app_token, private_key)

ziggeo.videos().create(file = video_file)