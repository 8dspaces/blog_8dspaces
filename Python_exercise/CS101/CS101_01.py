#coding: utf-8
#import urllib2
import requests

def get_all_links(page):
    
    links = []
    begin_link = page.find("<a href=")
    while begin_link > 0:
        start_quote = page.find('"', begin_link)
        end_quote = page.find('"', start_quote+1)
        url = page[start_quote+1: end_quote]
        links.append(url)
        page = page[end_quote+1:]
        begin_link = page.find("<a href=")
        
    for i in links:
        print i
        
        
if __name__ == "__main__":
    
    #page = urllib2.urlopen("http://www.douban.com")
    page = requests.get("http://www.douban.com")
    get_all_links(page.text)