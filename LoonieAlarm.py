#!/usr/bin/env python
import sys
import time
import datetime
import subprocess



def currentTime():
	sectimes=((int(time.time())+68400)%86400)
	mintimes = int(sectimes)-(int(sectimes)%60)
	return mintimes	 


t = raw_input('What time would  you like to get up? ')
if "pm" in t:
	night=t.split("pm")
	
	if ":" in t:
		a=night[0].split(":")
		secsH=int(a[0])*60*60
		secsM=int(a[1])*60
		secs=int(secsH)+int(secsM)+43200
	else:
		secs=(int(night[0])*60*60)+43200
else :
	morn=t.split("am")
	if ":" in morn[0]:
		b=morn[0].split(":")
		secsH=int(b[0])*60*60
		secsM=int(b[1])*60
		secs=int(secsH)+int(secsM)
	else:
		secs=(int(morn[0])*60*60)	

sectimes=((int(time.time()))+68400)%86400
mintimes = int(sectimes)-(int(sectimes)%60)
while secs != mintimes:
	time.sleep(1)
	mintimes = currentTime()

videos=["/Users/Ryantrapp/Desktop/Optum/test.mp4",
	"/Users/Ryantrapp/Desktop/Optum/test.mp4",
	"/Users/Ryantrapp/Desktop/Optum/test.mp4",
	"/Users/Ryantrapp/Desktop/Optum/test.mp4",
	"/Users/Ryantrapp/Desktop/Optum/test.mp4"]
	
subprocess.Popen(['open',videos[random.randint(0,4)])
