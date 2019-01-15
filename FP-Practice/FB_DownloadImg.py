import urllib3
import re
import chardet

def getHtml(url):
    http = urllib3.PoolManager() #type: urllib3.poolmanager.PoolManager
    response = http.urlopen("", url) #type: urllib3.response.HTTPResponse
    html = response.read() #type: bytes
    print(html.__len__())
    return html

def getImg(html):
    encode_type = chardet.detect(html) #type: dict
    encode_type['encoding'] = 'utf-8'
    html = html.decode(encode_type['encoding'])
    reg = 'src="(.+?\.jpg)" alt='
    imgre = re.compile(reg) #type: re.Pattern
    imglist = re.findall(imgre, html, 0)
    x = 0
    for imgurl in imglist:
        urllib3.urlretrieve(imgurl, '%s.jpg' % x)
        x+=1
    return imglist

html = getHtml("http://pic.yxdown.com/list/0_0_1.html")

print(getImg(html))