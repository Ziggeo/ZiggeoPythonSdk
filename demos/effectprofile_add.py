import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print ("Error\n")
	print ("Usage: $>python add_effect_profile.py YOUR_API_TOKEN YOUR_PRIVATE_KEY \"EFFECT_TITLE\" [EFFECT_TOKEN]\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
effect_title = sys.argv[3]
if(sys.argv==5):
	effect_token = sys.argv[4]
else:
	effect_token = ""

ziggeo = Ziggeo(api_token, private_key)
if(effect_token ==""):
	print (ziggeo.effectProfiles().create({"title": effect_title, "token": None}))
else:
	print (ziggeo.effectProfiles().create({"title": effect_title, "token": effect_token}))
