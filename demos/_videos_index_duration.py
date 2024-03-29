import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print("Error\n")
	print("Usage: $>python _videos_index_duration.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]

total_duration = 0.0
count_duration = 0.0

ziggeo = Ziggeo(app_token, private_key)

def indexVideos(skip = 0):
	global count_duration, total_duration
	video_list = ziggeo.videos().index({"limit":100, "skip":skip})
	for video in video_list:
		if video['duration'] is not None:
			total_duration += video['duration']
			count_duration += 1
		
	if(len(video_list) > 0):
		indexVideos(skip + 100)
	pass

indexVideos(0)

print("Total Duration = {:.2f} seconds, Average Duration {:.2f} seconds.".format(total_duration, ( total_duration /count_duration )))