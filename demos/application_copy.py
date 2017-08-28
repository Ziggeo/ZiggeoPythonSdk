import sys, os

from Ziggeo import Ziggeo

if(len(sys.argv) < 5):
    print ("Error\n")
    print ("Usage: $>python application_copy.py SOURCE_API_TOKEN SOURCE_PRIVATE_KEY TARGET_API_TOKEN TARGET_PRIVATE_KEY\n")
    sys.exit()

from pprint import pprint

source_api_token = sys.argv[1]
source_private_key = sys.argv[2]
target_api_token = sys.argv[3]
target_private_key = sys.argv[4]
ziggeo_source = Ziggeo(source_api_token, source_private_key)
ziggeo_target = Ziggeo(target_api_token, target_private_key)

def indexVideos(skip=0):
    video_list = ziggeo_source.videos().index({"limit":2, "skip":skip})
    for video in video_list:
        download_video_token = video["token"]
        print ("downloading video "+ download_video_token)
        stream_token = video["original_stream"]["token"]
        file_name = download_video_token + "_" + stream_token + '.' + video["original_stream"]["video_type"]
        file_name = file_name.encode("ascii", 'ignore')
        # We are using "wb" for write binary. To prevent windows from using write as non binary
        file = open(file_name, "wb")
        downloaded_file = ziggeo_source.streams().download_video(download_video_token, stream_token)

        try:
            file.write(downloaded_file)
        except UnicodeEncodeError as e:
            print("Video " + download_video_token + " can't be upload due to unicode error.")
            file.close()
            delete_file(file_name)
            continue

        file.close()
        uploadVideo(file_name)
        delete_file(file_name)

    if(len(video_list) > 0):
        indexVideos(skip + 2)
    pass


def uploadVideo(file_name = ""):
    print ("uploading video " + str(file_name))
    ziggeo_target.videos().create(file = file_name)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("Video, %s was removed from local directory." % filename)
    else:
        print("Sorry, I can not remove %s file." % filename)

indexVideos(0)
