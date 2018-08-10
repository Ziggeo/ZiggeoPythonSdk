import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print "Error\n"
	print "Usage: $>python video_expiration_days_bulk.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDTOKEN1,VIDTOKEN2 EXPIRATION\n" # Expiration days are integer
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]
expiration_days = sys.argv[4]

ziggeo = Ziggeo(api_token, private_key)
arguments={}
arguments['tokens_or_keys'] = video_token
arguments["expiration_days"] = expiration_days
print ziggeo.videos().update_bulk(arguments)