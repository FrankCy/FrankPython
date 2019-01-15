import urllib3

url = "http://www.baidu.com"
http = urllib3.PoolManager() # type: urllib3.poolmanager.PoolManager
print(http.__class__)
response1 = http.urlopen('GET', url) # type: urllib3.response.HTTPResponse
print("####### 方法1 #######")
# 获取状态码，200表示成功
print(response1.status)
# 获取网页内容的长度
print(response1.version)

print("####### 方法2 #######")
response2 = http.request('GET', url) # type: urllib3.response.HTTPResponse

from urllib import parse
# url转码操作，只有转码后浏览器才会识别该url
kw = {'name': '中国'}
res = parse.urlencode(kw)
print(res)
res2 = parse.unquote(res)
print(res2)
# 结果如下：
# name=E5%B0%8F%E5%8F%AF
# name=中国

