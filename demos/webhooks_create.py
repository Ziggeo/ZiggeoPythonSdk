import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 6):
    print ("Error\n")
    print ("Usage: $>python webhooks_create.py YOUR_API_TOKEN YOUR_PRIVATE_KEY WEBHOOK_URL ENCODING EVENTS\n")
    print ("Example: $>python webhooks_create.py 1234567890abcdef 1234567890abcdef http://yoursite.com jsonheader video_create,video_delete\n")
    sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
target_url = sys.argv[3]
encoding = sys.argv[4] # jsonheader, json, or form
events = sys.argv[5]

ziggeo = Ziggeo(api_token, private_key)

arguments = {}
arguments['target_url'] = target_url
arguments['encoding'] = encoding
arguments['events'] = events

print(arguments)

webhooks = ziggeo.webhooks().create(arguments)

print(webhooks)