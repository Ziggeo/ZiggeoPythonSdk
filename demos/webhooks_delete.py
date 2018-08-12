import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
    print ("Error\n")
    print ("Usage: $>python webhooks_delete.py YOUR_API_TOKEN YOUR_PRIVATE_KEY WEBHOOK_URL \n")
    print ("Example: $>python webhooks_delete.py 1234567890abcdef 1234567890abcdef http://yoursite.com \n")
    sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
target_url = sys.argv[3]

ziggeo = Ziggeo(api_token, private_key)

arguments = {}
arguments['target_url'] = target_url

ziggeo.webhooks().delete(arguments)