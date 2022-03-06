import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 6):
	print("Error\n")
	print("Usage: $>python webhooks_create.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY WEBHOOK_URL ENCODING EVENTS\n")
	print("Example: $>python webhooks_create.py 1234567890abcdef 1234567890abcdef http://yoursite.com jsonheader video_create,video_delete\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
target_url = sys.argv[3]
encoding = sys.argv[4] # jsonheader, json, or form
events = sys.argv[5]

ziggeo = Ziggeo(app_token, private_key)

arguments = {}
arguments['target_url'] = target_url
arguments['encoding'] = encoding
arguments['events'] = events

print(arguments)

webhooks = ziggeo.webhooks().create(arguments)

print(webhooks)