import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print ("Error\n")
	print ("Usage: $>python download_all_videos.py YOUR_API_TOKEN YOUR_PRIVATE_KEY\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
ziggeo = Ziggeo(api_token, private_key)
def indexVideos(skip=0):
	yey = 0
	video_list = ziggeo.videos().index({"limit":100, "skip":skip})
	for video in video_list:
		download_video_token = video["token"]
		print ("downloading video "+download_video_token)
		stream_token = video["default_stream"]["token"]
		file_name = download_video_token+"_"+stream_token+'.'+video["default_stream"]["video_type"]
		# We are using "wb" for write binary. To prevent windows from using write as non binary
		file = open(file_name, "wb")
		downloaded_file = ziggeo.streams().download_video(download_video_token, stream_token)
		file.write(downloaded_file)
		file.close()
	if(len(video_list) > 0):
		indexVideos(skip+100)
	pass
indexVideos(0)
