import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print("Error\n")
	print("Usage: $>python _videos_index_browser.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]

browsers = {}
total_browser = 0.0

ziggeo = Ziggeo(app_token, private_key)

def indexVideos(skip = 0):
	global browsers, total_browser
	video_list = ziggeo.videos().index({"limit":100, "skip":skip})
	for video in video_list:
		if video['device_info'] is not None:
			browser = video['device_info']['browser']
		else :
			browser = 'Unknown'

		if  browsers.get(browser) is None:
			browsers[browser] = 1
		else :
			browsers[browser] = browsers[browser] + 1
			
		total_browser += 1
	if(len(video_list) > 0):
		indexVideos(skip + 100)
	pass

indexVideos(0)

for browser in browsers:
	print("Browser {:s}: {:d} ({:.2f}%)".format(browser, browsers[browser], (browsers[browser] / total_browser) * 100 ))