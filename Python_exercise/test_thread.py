# coding: utf-8

from threading import Thread
import time
import urllib2

class GetUrlThread(Thread):
    def __init__(self, url):
        self.url = url
        # or super(GetUrlThread, self).__init__()
        Thread.__init__(self)
    def run(self):
        resp = urllib2.urlopen(self.url)
        print self.url, resp.getcode()

def get_response_2():
    urls = [
            "http://www.amazon.com",
            "http://www.baidu.com",
            "http://www.douban.com",
            "http://www.reddit.com",
    ]
    start = time.time()
    threads = []
    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print "Elapsed time: %s" % (time.time()-start)

def get_response_1():
    urls = [
        'http://www.amazon.com',
        'http://www.ebay.com',
        'http://www.alibaba.com',
        'http://www.reddit.com'
    ]
    start = time.time()
    for url in urls:
        print url
        resp = urllib2.urlopen(url)
        print resp.getcode()
    print "Elapsed time: %s" % (time.time()-start)
 

    
#get_response_1()
get_response_2()
