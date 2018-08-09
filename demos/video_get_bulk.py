import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print ("Error\n")
	print ("Usage: $>python video_get_bulk.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_TOKEN1,VIDEO_TOKEN2 \n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_token = sys.argv[3]

ziggeo = Ziggeo(api_token, private_key)

bulk_arguments = {}
bulk_arguments["tokens_or_keys"] = video_token

print (ziggeo.videos().get_bulk(bulk_arguments))
