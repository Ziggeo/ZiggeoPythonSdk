import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print ("Error\n")
	print ("Usage: $>python delete_all_rejected_videos.py YOUR_API_TOKEN YOUR_PRIVATE_KEY\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
ziggeo = Ziggeo(api_token, private_key)
def indexVideos(skip=0):
	yey = 0
	video_list = ziggeo.videos().index({"limit":100, "skip":skip,"approved":"REJECTED"})
	for video in video_list:
		delete_video_token = video["token"]
		print ("deleting video "+delete_video_token)
		ziggeo.videos().delete(delete_video_token)
	if(len(video_list) > 0):
		indexVideos(skip+100)
	pass
indexVideos(0)
