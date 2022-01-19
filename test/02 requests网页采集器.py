#UA: User-Agent(请求身份标识)
#UA伪装：门户网站的服务器会检测对应请求的载体身份标示，如果检测到请求载体的身份标示为某一浏览器，则认为是正常的请求。但是，如果检测到请求
#载体身份标示不是基于某一浏览器，则表示该请求为不正常的请求

#爬虫程序一定要进行UA伪装

import requests

if __name__ == "__main__":
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    url = "https://www.sogou.com/web"
    #处理url携带的参数: 封装到字典中
    kw = input('enter a word:')
    param = {
        'query' : kw
    }
    #对指定的url发起的请求对应的url是携带参数的
    response = requests.get(url=url,params=param,headers=headers)

    page_text= response.text

    filename = kw + '.html'
    with open(filename,'w',encoding='utf-8') as fp:
        fp.write(page_text)