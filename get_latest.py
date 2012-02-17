#!/usr/bin/env python

'''
Get latest updats to gta mailing list
'''

import feedparser
import requests
import codecs
import StringIO
import sys

def get_latest_remote_id(rss_url):
    feed = feedparser.parse(rss_url)
    return int(feed.values()[10][0]['id'].split('/')[-1])
def get_latest_local_id(fname):
    return int(open(fname, 'r').read())

def download_archive(url, start, stop, step):
    current = start
    buff = StringIO.StringIO()
    while True:
        dl_url = "%s/%d/%d" % (url, current, stop if current + step > stop else current + step)
        out = requests.get(dl_url)
        if out.ok:
            buff.write(out.text)
            if current == stop:
                return buff.getvalue()
            else:
                current = stop if current + step > stop else current + step
        else:
            return False
        
gmane_rss = "http://rss.gmane.org/messages/complete/gmane.org.user-groups.linux.tolug"
latest_id_file = 'latest_msg'
archive_base_url = 'http://download.gmane.org/gmane.org.user-groups.linux.tolug'
datafile = 'tlug_archive.txt'
step = 200

latest_remote = get_latest_remote_id(gmane_rss)
latest_local = get_latest_local_id(latest_id_file)

if latest_remote > latest_local:
    print  latest_local, latest_remote
    append =  download_archive(archive_base_url, latest_local, latest_remote+1, step)
    if not append:
        print "error downloading archive"
        sys.exit(2)
    f_append = codecs.open(datafile, 'a','utf-8')
    f_append.write(append)
    f_append.close()
    open(latest_id_file,'w').write(str(latest_remote))
else:
    print "Up to date"
    sys.exit(1)
