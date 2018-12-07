import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print ("Error\n")
	print ("Usage: $>python _videos_index_orientation.py YOUR_API_TOKEN YOUR_PRIVATE_KEY\n")
	sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
count_landscape = 0.0
count_portrait = 0.0
ziggeo = Ziggeo(api_token, private_key)
def indexVideos(skip=0):
	global count_landscape, count_portrait
	video_list = ziggeo.videos().index({"limit":100, "skip":skip})
	for video in video_list:
		width = video['streams'][0]['video_width']
		height = video['streams'][0]['video_height']
		if ( width > height) :
			count_landscape += 1	
		else :
			count_portrait += 1
	if(len(video_list) > 0):
		indexVideos(skip+100)
	pass
indexVideos(0)
pr_portrait = (count_portrait/(count_landscape+count_portrait))*100
pr_landscape = (count_landscape/(count_landscape+count_portrait))*100
print("Portrait Count = {:.0f} Portrait Percentage {:.2f}%".format(count_portrait, pr_portrait))
print("Landscape Count = {:.0f} Landscape Percentage {:.2f}%".format(count_landscape, pr_landscape))