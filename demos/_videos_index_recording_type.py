import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print("Error\n")
	print("Usage: $>python _videos_index_recording_type.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]

webrtc_screen_recordings = 0
webrtc_camera_recordings = 0
file_uploads_or_camera_app = 0

ziggeo = Ziggeo(app_token, private_key)

def indexVideos(skip = 0):
	global webrtc_screen_recordings, webrtc_camera_recordings, file_uploads_or_camera_app

	video_list = ziggeo.videos().index({"limit":100, "skip":skip})

	for video in video_list:
		if video['device_info'] is not None:
			media_source_value = video['device_info']['media_source']
			if media_source_value == 'screen':
				webrtc_screen_recordings += 1
			elif media_source_value == 'record':
				webrtc_camera_recordings += 1
			elif media_source_value == "upload":
				file_uploads_or_camera_app += 1

	if(len(video_list) > 0):
		indexVideos(skip + 100)
	pass


indexVideos(0)

print("In Browser Screen recordings:",webrtc_screen_recordings)
print("In Browser Camera recordings:",webrtc_camera_recordings)
print("File Uploads OR Default Camera App recordings:",file_uploads_or_camera_app)