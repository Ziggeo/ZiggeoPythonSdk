import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print ("Error\n")
	print ("Usage: $>python get_effect_profiles.py YOUR_API_TOKEN YOUR_PRIVATE_KEY\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]

index_arguments = {}
index_arguments["limit"] = 50
ziggeo = Ziggeo(api_token, private_key)

print (ziggeo.effectProfiles().index(index_arguments))
