import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 5):
	print "Error\n"
	print "Usage: $>python add_effect_profile.py YOUR_API_TOKEN YOUR_PRIVATE_KEY \"EFFECT_TITLE\" [EFFECT_TOKEN] \"EFFECT_FILTER\"\n"
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
effect_title = sys.argv[3]
effect_token = sys.argv[4]
effect_filter = sys.argv[5]
if(effect_token==""):
	effect_token = sys.argv[4]
else:
	effect_token = ""

ziggeo = Ziggeo(api_token, private_key)
if(effect_token ==""):
	effect = ziggeo.effectProfiles().create({"title": effect_title, "token": None})
else:
	effect = ziggeo.effectProfile().create({"title": effect_title, "token": effect_token})

filter_arguments = {}
filter_arguments["filter"] = effect_filter
ziggeo.effectProfileProcess().create_filter_process(effect["token"], filter_arguments)