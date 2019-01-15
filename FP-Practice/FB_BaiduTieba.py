# 处理HTTP请求,在python2中是urllib2,在python3中是urllib.request
from urllib import request, parse


def loadPage(url, filename):
    '''
           作用：根据url发送请求，获取服务器响应文件
           url：需要爬取的url地址
           filename: 文件名
    '''
    print("[LOG]: 正在下载" + filename)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6"}
    # 构造请求对象
    req = request.Request(url, headers=headers)
    # 发送请求，返回响应结果
    response = request.urlopen(req)
    if response.getcode() == 200:
        return response.read()
    else:
        print("[ERR]: 下载失败...")


def writePage(html, filename):
    """
          作用：保存服务器响应文件到本地磁盘文件里
          html: 服务器响应文件
          filename: 本地磁盘文件名
    """
    print("[LOG]: 正在写入" + filename)
    with open(filename, "wb") as f:
        f.write(html)


def tiebaSpider(url, beginPage, endPage):
    """
            作用：负责处理url，分配每个url去发送请求
            url：需要处理的第一个url
            beginPage: 爬虫执行的起始页面
            endPage: 爬虫执行的截止页面
    """
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        # 对pn进行转码后，才能在浏览器中识别
        keyword = parse.urlencode({"pn": pn})
        fullurl = url + "&" + keyword
        print(fullurl)
        # 爬取到的数据存放的文件名称
        filename = "第" + str(page) + "页.html"
        html = loadPage(fullurl, filename)
        writePage(html, filename)


if __name__ == "__main__":
    tiebaName = input("请输入需要爬取的贴吧名：")
    beginPage = int(input("请输入爬取的起始页："))
    endPage = int(input("请输入爬取的终止页: "))

    # "https://tieba.baidu.com/f? kw=%E6%9D%8E%E6%AF%85&pn=50"
    baseURL = "http://tieba.baidu.com/f?"
    keyword = {"kw": tiebaName}
    kw = parse.urlencode(keyword)
    url = baseURL + kw
    tiebaSpider(url, beginPage, endPage)

