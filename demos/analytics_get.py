import os, sys
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 4):
	print("Error\n")
	print("Usage: $>python analytics_get.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY QUERY\n")
	print("Example: $>python analytics_get.py 1234567890abcdef 1234567890abcdef device_view_by_os\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
query = sys.argv[3]

ziggeo = Ziggeo(app_token, private_key)

ts = time.time()

arguments = {}
arguments['from'] = 0
arguments['to'] = ts
arguments['query'] = query

print(ziggeo.analytics().get(arguments))