import  requests
import json
if __name__ == '__main__':
    url='https://movie.douban.com/j/chart/top_list'#url有参数，最好用字典形式封装
    params = {
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start':'1', #从第60部开始
        'limit':'20'  #获取的数量
    }

    headers ={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    response=requests.get(url=url,params=params,headers=headers)
    list_data = response.json()

    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
