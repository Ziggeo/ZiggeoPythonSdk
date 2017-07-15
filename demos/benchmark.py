import sys, time

from Ziggeo import Ziggeo
import json
if(len(sys.argv) < 5):
	print "Error\n"
	print "Usage: $>python benchmark.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_FILE OPERATION_TIME\n"
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_file = sys.argv[3]
ops_time = int(sys.argv[4])

times = {'upload': 0, 'download': 0, 'delete':0}
ziggeo = Ziggeo(api_token, private_key)

upload_time = time.time()
for i in range(ops_time):
	ziggeo.videos().create(file = video_file)
upload_time = time.time()-upload_time
times['upload'] = upload_time/ops_time

print "Upload: "+str(times['upload'])