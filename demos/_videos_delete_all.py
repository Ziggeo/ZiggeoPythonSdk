import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print("Error\n")
	print("Usage: $>python _videos_delete_all.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]

ziggeo = Ziggeo(app_token, private_key)

def indexVideos(skip = 0):
	yey = 0
	video_list = ziggeo.videos().index({"limit":100, "skip":skip})
	for video in video_list:
		delete_video_token = video["token"]
		print("deleting video " + delete_video_token)

		ziggeo.videos().delete(delete_video_token)
	if(len(video_list) > 0):
		indexVideos(skip + 100)
	pass

indexVideos(0)