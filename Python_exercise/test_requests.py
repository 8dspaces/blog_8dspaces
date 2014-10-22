#import requests
import re 

#url = 'https://api.github.com/users/kennethreitz/repos?page=1&per_page=10'
#url = r'http://www.douban.com/online/11717703/album/127530212/?start=0'
#r = requests.head(url=url)


#print r.links["next"]
#print r.links["last"]
#print r.links


mystr = "security/afafsff/?ip=123.4.56.78&id=45"
m = re.search(r".*\?ip=([1-9\.]+)\&.*", mystr)
print m.group(1)
