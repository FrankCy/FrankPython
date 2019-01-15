"""
爬指定地址下的所有图片
"""
#导入urllib3
import urllib3
#设置disable_warnings避免https整数导致的错误
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#定义函数
def getHtml(url):
    http = urllib3.PoolManager() # type: urllib3.poolmanager.PoolManager
    print(http.__class__)
    response = http.urlopen("", url) # type: urllib3.response.HTTPResponse
    html = response.read()
    return html

#调用函数，并输入源地址
html = getHtml("http://tieba.baidu.com/p/5993522944")

#输出响应信息
print(html)