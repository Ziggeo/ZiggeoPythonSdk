import os, sys

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print("Error\n")
	print("Usage: $>python _metaprofiles_create_with_audio_transcription_process.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY METAPROFILE_TITLE\n")
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]
metaprofiles_title = sys.argv[3]

ziggeo = Ziggeo(app_token, private_key)

arguments = {}
arguments['title'] = metaprofiles_title

metaprofiles = ziggeo.metaProfiles().create(arguments)

metaprofiles_process = ziggeo.metaProfileProcess().create_audio_transcription_process(metaprofiles['token'])

print(metaprofiles_process)