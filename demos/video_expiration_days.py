import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 5):
	print ("Error\n")
	print ("Usage: $>python video_expiration_days.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN EXPIRATION_DAYS\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]
expiration_days = sys.argv[4]

ziggeo = Ziggeo(api_token, private_key)
update_arguments = {}
update_arguments["expiration_days"] = int(expiration_days)
print (ziggeo.videos().update(video_token, update_arguments))
