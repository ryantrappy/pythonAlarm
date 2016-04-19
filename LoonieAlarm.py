#!/usr/bin/env python
import sys
import time
import datetime
import vlc
import numpy as np


def currentTime():
	sectimes=((int(time.time())+68400)%86400)
	mintimes = int(sectimes)-(int(sectimes)%60)
	return mintimes	 


Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new_path('./valley1.mov')
player.set_media(Media)
player.play()



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

print secs

sectimes=((int(time.time()))+68400)%86400
mintimes = int(sectimes)-(int(sectimes)%60)
print mintimes
while secs != mintimes:
	time.sleep(5)
	mintimes = currentTime()
	print mintimes
print "its time to wake up"

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new_path('./valley1.mov')
player.set_media(Media)
player.play()
