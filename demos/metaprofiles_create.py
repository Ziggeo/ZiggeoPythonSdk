import sys

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
    print ("Error\n")
    print ("Usage: $>python metaprofiles_create.py YOUR_API_TOKEN YOUR_PRIVATE_KEY METAPROFILE_TITLE\n")
    sys.exit()

api_token = sys.argv[1]
private_key = sys.argv[2]
metaprofiles_title = sys.argv[3]
ziggeo = Ziggeo(api_token, private_key)

arguments = {}
arguments['title'] = metaprofiles_title
metaprofiles = ziggeo.metaProfiles().create(arguments)

print(metaprofiles)