import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 5):
	print "Error\n"
	print "Usage: $>python add_effect_profile.py YOUR_API_TOKEN YOUR_PRIVATE_KEY \"EFFECT_TITLE\"  \"FILE\" \"VERTICAL\" \"HORIZONTAL\" \"SCALE\"\n"
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
effect_title = sys.argv[3]
watermark_file = sys.argv[4]
watermark_vertical = sys.argv[5]
watermark_horizontal = sys.argv[6]
watermark_scale = sys.argv[7]


ziggeo = Ziggeo(api_token, private_key)

effect = ziggeo.effectProfiles().create({"title": effect_title, "token": None})


filter_arguments = {}

filter_arguments["vertical_position"] = float(watermark_vertical)
filter_arguments["horizontal_position"] = float(watermark_horizontal)
filter_arguments["video_scale"] = float(watermark_scale)
ziggeo.effectProfileProcess().create_watermark_process(effect["token"], filter_arguments, watermark_file)