import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print("Error\n")
	print("Usage: $>python videos_stats_bulk.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN1,VIDEO_TOKEN2 \n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]

ziggeo = Ziggeo(app_token, private_key)

bulk_arguments = {}
bulk_arguments["tokens_or_keys"] = video_token

print(ziggeo.videos().stats_bulk(bulk_arguments))