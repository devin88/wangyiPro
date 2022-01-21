import  requests
import json
#逆光飞翔 听见天堂  田埂上的梦 国王的演讲
if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    data = {
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn':''
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }
    id_list=[]
    json_ids = requests.post(url=url,headers=headers,data=data).json()

    for dic in json_ids['list']:
        id_list.append(dic['ID'])
    print(id_list)


    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id':id
        }

        detail_json = requests.post(url =url,headers=headers,data=data).json()
    print(detail_json)
