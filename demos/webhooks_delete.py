import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print("Error\n")
	print("Usage: $>python webhooks_delete.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY WEBHOOK_URL \n")
	print("Example: $>python webhooks_delete.py 1234567890abcdef 1234567890abcdef http://yoursite.com \n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
target_url = sys.argv[3]

ziggeo = Ziggeo(app_token, private_key)

arguments = {}
arguments['target_url'] = target_url

ziggeo.webhooks().delete(arguments)