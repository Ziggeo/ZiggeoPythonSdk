import sys, time

from Ziggeo import Ziggeo
import json
if(len(sys.argv) < 5):
	print ("Error\n")
	print ("Usage: $>python benchmark.py YOUR_API_TOKEN YOUR_PRIVATE_KEY VIDEO_FILE OPERATION_TIME\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
video_file = sys.argv[3]
ops_time = int(sys.argv[4])

arguments = {}
arguments['tags'] = "benchmark"
ziggeo = Ziggeo(api_token, private_key)
videos= []
upload_time = time.time()
for i in range(ops_time):
	video = ziggeo.videos().create(arguments,file = video_file ) #adding 'benchmark' tag for uploaded video
	videos.append(video['token'])

upload_time = time.time()-upload_time
upload_time = upload_time/ops_time

download_time = time.time()
for v in videos:
	ziggeo.videos().download_video(v)
download_time = time.time()-download_time

delete_time = time.time()
for v in videos:
	ziggeo.videos().delete(v)

delete_time = time.time()-delete_time
delete_time = delete_time/ops_time

print ("Upload: "+str(upload_time))
print ("Download: "+str(download_time))
print ("Delete: "+str(delete_time))
