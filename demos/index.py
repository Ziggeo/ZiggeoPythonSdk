import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print "Error\n"
	print "Usage: $>python index.py YOUR_API_TOKEN YOUR_PRIVATE_KEY\n"
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
ziggeo = Ziggeo(api_token, private_key)
# 'limit' will limit how much index operation will fetch the videos. default 50 max 100
video_list = ziggeo.videos().index({"limit":100})
for video in video_list:
	print video