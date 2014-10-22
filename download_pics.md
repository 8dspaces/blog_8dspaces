用python批量下载图片 -- Simple example
====

### 方法一: urllib

主要用到了自带的urllib 模块

+ **urllib.urlopen(url)**
+ **urllib.urlretrieve(url)**


#### Python Code: 

    import re
    import urllib


    def getHtml(url):
        page=urllib.urlopen(url)
        html=page.read()
        return html
        
    def getJpg(html):
        reg=r'src="(.*?\.jpg)" width'
        imgre=re.compile(reg)
        imglist=re.findall(imgre,html)
        x=0
        for imgurl in imglist:
                urllib. urlretrieve(imgurl,'%s.jpg' % x)
                x+=1
                
    html=getHtml("http://www.douban.com")
    print getJpg(html)

### 方法二：requests库

安装： `pip install requests`
用到的方法

+ **requests.get(url)**


####Python Code:

    def downloadImageFile(imgUrl):
        
        local_filename = imgUrl.split('/')[-1]  
        
        # here we need to set stream = True parameter
        r = requests.get(imgUrl, stream=True)   
        with open("/Users/mickqi/"+local_filename, 'wb') as f:  
            for chunk in r.iter_content(chunk_size=1024):  
                if chunk: # filter out keep-alive new chunks  
                    f.write(chunk)  
                    f.flush()  
            f.close()  
        print "Download Image File=", local_filename 

其他的参考，用requests读到html文件，用xml DOM方式来解析

    import requests  
    import lxml.html  
   
    page = requests.get('http://tieba.baidu.com/p/2166231880').text  
    doc = lxml.html.document_fromstring(page)  
    for idx, el in enumerate(doc.cssselect('img.BDE_Image')):  
        with open('%03d.jpg' % idx, 'wb') as f:  
            f.write(requests.get(el.attrib['src']).content)  
            
            