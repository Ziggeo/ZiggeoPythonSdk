import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print ("Error\n")
	print ("Usage: $>python video_list_all.py YOUR_API_TOKEN YOUR_PRIVATE_KEY\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
ziggeo = Ziggeo(api_token, private_key)
def indexVideos(skip=0):
	yey = 0
	video_list = ziggeo.videos().index({"limit":100, "skip":skip})
	for video in video_list:
		print (video)
	if(len(video_list) > 0):
		indexVideos(skip+100)
	pass
indexVideos(0)
