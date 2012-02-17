#!/usr/bin/env python

'''
Inefficiently fetch full copy of gtalug mailing list without hitting
PHP execution 30 second limit on the server
'''

import requests
from time import time, sleep
import codecs
import StringIO
maxget = 57370
current = 0
orig_step = 2000

target = codecs.open('tlug_data.txt', 'a', 'utf-8')

tlug_url = 'http://download.gmane.org/gmane.org.user-groups.linux.tolug'

step = orig_step
while current <= maxget:
	req_start = time()
	buff = StringIO.StringIO()
	dl_url = "%s/%d/%d" % (tlug_url, current, current+step % (maxget + 1))
	print dl_url
	out = requests.get(dl_url)
	if out.ok:
		buff.write(out.text)
		del out
	else:
		print "Network error, retrying", out
		del out
		continue

	interval = time() - req_start
	print "Interval: ", interval
	if interval < 30:
		target.write(buff.getvalue())
		current += step
		if step != orig_step:
			step = int((1.5*step) % orig_step)
	else:
		step /= 2
	buff.close()

target.close()