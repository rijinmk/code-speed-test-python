import urllib
import time
import sys
times = []
tc = int(sys.argv[1])
for i in range(tc):
	print 'Test case #',i+1,'...'
	start = time.time()
	urllib.urlopen('https://github.com/rijinmk/code-speed-test-python/raw/master/onemb').read()
	times.append(time.time() - start)
	time.sleep(0.1)
s = 0
for i in times:
	s += (1/i)*8
internet_speed = s/tc
print "Your internet download speed is approximately: ", internet_speed, "Mb/s"
