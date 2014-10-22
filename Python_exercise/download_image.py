# coding: utf-8

import urllib, re
global i

def get_html(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html
    
def get_img(html):
    global i
    reg = r'src="(.*?\.jpg)"'
    imgre = re.compile(reg)
    
    imglist = re.findall(imgre,html)
    
    for imgurl in imglist:
        if imgurl.find("thumb") > 0:
            imgurl = imgurl.replace("thumb","photo")
            urllib.urlretrieve(imgurl,r"c:\temp\test2\%s.jpg" % i)
            i += 1
        else:
            imglist.remove(imgurl)
    
if __name__ == "__main__":
    global i
    i = 0
    images_per_page = 90
    page_end = 1260 + images_per_page
    
    for x in range(0,page_end,images_per_page):
        url = r"http://www.douban.com/online/11717703/album/127530212/?start=%s" % x
        #url = r"http://www.douban.com/photos/album/127711572/?start=%s" % x
        html = get_html(url)
        get_img(html)