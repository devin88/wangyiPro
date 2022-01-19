import requests
import json

if __name__ == "__main__":
    #指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    #post请求参数处理
    word = input("enter a word:")
    data = {
        'kw' : word
    }
    #请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    #获取响应数据,json()方法返回的是一个字典对象（如果确认响应数据是json类型的，才可以使用方法进行对象返回）
    dic_obj = response.json()
    print(dic_obj)
    filename = word + '.json'
    fp=open(filename,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)   #ensure_ascii 获取的是中文，因此写为False