#!/usr/bin/env python
import sys
import time
import webbrowser
import random


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

print secs

sectimes=((int(time.time()))+68400)%86400
mintimes = int(sectimes)-(int(sectimes)%60)
print mintimes
while secs != mintimes:
	time.sleep(1)
	mintimes = currentTime()
print "its time to wake up"
videos=["https://www.youtube.com/watch?v=9x_FzCWl2nc&list=PL7spvnQF9O-ia-SPOzQNReIJH4xH8bVWE&index=3",
	"https://www.youtube.com/watch?v=EykJCbu8jZw&list=PL7spvnQF9O-ia-SPOzQNReIJH4xH8bVWE&index=13",
	"https://www.youtube.com/watch?v=9x_FzCWl2nc&list=PL7spvnQF9O-ia-SPOzQNReIJH4xH8bVWE&index=2",
	"https://www.youtube.com/watch?v=4xOFGVD4yNI&index=25&list=PL7spvnQF9O-ia-SPOzQNReIJH4xH8bVWE",
	"https://www.youtube.com/watch?v=ZJJHL5p9UIE&list=PL7spvnQF9O-ia-SPOzQNReIJH4xH8bVWE&index=44"]
	
webbrowser.open(videos[random.ranint(0,4)])
