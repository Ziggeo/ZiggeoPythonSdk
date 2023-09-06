#This demo gives the user capability to enter a date and all the videos older than this date will be deleted.
import os, sys
import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

sys.path.append("..")

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print("Error\n") 
	print("Usage: $>python _delete_videos_older_than_input_date.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY")  
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]

ziggeo = Ziggeo(app_token, private_key)

def InputuserDate(): 
#Will prompt the user to enter Target Date and validate it. Call Index Videos at the end.

	try:
		global TargetDate 
		TargetDate = datetime.datetime.strptime(input("Enter Target Date in dd/mm/yyyy format, for example 06/12/2021: "),"%d/%m/%Y").date() 
	except ValueError:
		print("Please enter a valid date")
		sys.exit()
	CurrentDate = datetime.date.today()

	Difference = CurrentDate - TargetDate 

	if(Difference.days < 0):
		print("You Cannot enter a date greater than today's date")
		sys.exit()
	indexVideos(0)

def indexVideos(skip = 0):
	video_list = ziggeo.videos().index({"limit":100,"skip":skip})
	for video in video_list:
		creationDate = datetime.date.fromtimestamp(video["created"])
		if creationDate < TargetDate:
			print(" The video " + video["token"] + " was created on "  + str(creationDate) + ",marking for deletion")
			ziggeo.videos().delete(video["token"])
	if(len(video_list) > 0):
		indexVideos(skip+100)
	pass
InputuserDate()