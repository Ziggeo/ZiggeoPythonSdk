#This demo gives you the capability to update expiration days for ALL your videos that currently have no expiration days as well as for the ones that have one. 
#Null for mode 1 and as difference of target date and creation date for mode 2.
import os, sys
import datetime

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)

sys.path.append("..")

from Ziggeo import Ziggeo

if(len(sys.argv) < 3):
	print("Error\n") 
	print("Usage: $>python _video_expiration_days_bulk_update_fix_date.py YOUR_APP_TOKEN YOUR_PRIVATE_KEY")  
	sys.exit()

app_token = sys.argv[1]
private_key = sys.argv[2]

ziggeo = Ziggeo(app_token, private_key)

mode = int(input("Please choose what you want to do. Press 1 if you want to clear any existing expiration settings on all videos. Press 2 if you want to set expiration_days to some date: "))

def InputuserDate(): 
#Will prompt the user to enter Target Date and validate it. Call Index Videos at the end.

	try:
		global TargetDate 
		TargetDate = datetime.datetime.strptime(input("Enter Target Date in dd/mm/yyyy format, for example 06/12/2021: "),"%d/%m/%Y").date() 

	except ValueError:
		print("Please enter a valid date")
		sys.exit()

	CurrentDate = datetime.date.today()

	Difference = TargetDate - CurrentDate

	if(Difference.days < 0):
		print("You Cannot enter a date less than today's date")
		sys.exit()

	indexVideos(0)

def indexVideos(skip = 0): 
# Will index videos and call update expiration days as per the user choice

	video_list = ziggeo.videos().index({"limit":100, "skip":skip})

	for video in video_list:

		CreationDate = datetime.date.fromtimestamp(video["created"])

		if mode == 1:
			NewExpirationDays = None			
		else:
			NewExpirationDays = (TargetDate - CreationDate).days

		UpdateExpirationDays(video["token"],NewExpirationDays)

	if(len(video_list) > 0):
		indexVideos(skip + 100)
	pass

def UpdateExpirationDays(video_token,NewExpirationDays):
#Will update each video as per the mode chosen
	arguments={}
	arguments['tokens_or_keys'] = video_token
	arguments["expiration_days"] = NewExpirationDays
	print("Updating video " + video_token + " setting expiration days to " + str(NewExpirationDays)) 
	ziggeo.videos().update_bulk(arguments)

if mode == 1:
	indexVideos(0)
elif mode == 2:
	InputuserDate()