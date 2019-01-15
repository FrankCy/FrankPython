#coding = utf-8
from urllib import request
import re
import chardet

def getHtml(url):
    page = request.urlopen(url) # type: http.client.HTTPResponse
    html = page.read()
    return html

def getImg(html):
    encode_type = chardet.detect(html)  # type: dict
    encode_type['encoding'] = 'gb2312'
    html = html.decode(encode_type['encoding'])
    reg = 'src="(.+?\.jpg)" alt='
    imgre = re.compile(reg)  # type: re.Pattern
    imglist = re.findall(imgre, html, 0)
    x = 0
    for imgurl in imglist:
        request.urlretrieve(imgurl, '%s.jpg' % x)
        x+=1
    return imglist

html = getHtml("http://desk.zol.com.cn")

print(getImg(html))
