# 导入urllib 库下request模块
from urllib import request

url = "http://www.baidu.com"

# IE 9.0 的 User-Agent
user_agent = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"}
req = request.Request(url, headers=user_agent)

# 也可以通过调用Reques.add_header() 添加/修改一个特定的header为长链接
req.add_header("Connection", "keep-alive")

# 也可以通过调用Request.get_header()来查看header信息
# req.get_header(header_name="Connection")

response = request.urlopen(req)

print(response.code)  # 可以查看响应状态码
# 网页源代码
html = response.read()

print(html)
