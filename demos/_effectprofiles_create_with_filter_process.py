import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 5):
	print "Error\n"
	print "Usage: $>python _effectprofiles_create_with_filter_process.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY \"EFFECT_TITLE\" [EFFECT_TOKEN] \"EFFECT_FILTER\"\n"
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
effect_title = sys.argv[3]
effect_token = sys.argv[4]
effect_filter = sys.argv[5]

if(effect_token==""):
	effect_token = sys.argv[4]
else:
	effect_token = ""

ziggeo = Ziggeo(app_token, private_key)

if(effect_token == ""):
	effect = ziggeo.effectProfiles().create({"title": effect_title, "token": None})
else:
	effect = ziggeo.effectProfiles().create({"title": effect_title, "token": effect_token})

filter_arguments = {}
filter_arguments["filter"] = effect_filter

ziggeo.effectProfileProcess().create_filter_process(effect["token"], filter_arguments)