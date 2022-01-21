import requests

#需求：爬取糗事百科的图片

if __name__ == '__main__':
    url = 'https://pic.qiushibaike.com/system/pictures/12172/121721055/medium/9osvy4zsu4nn6t7v.jpg'
    #图片是二进制数据，因此用content 而不用text
    #content 二进制数据   text 字符串   json() 对象
    img_data = requests.get(url=url).content

    with open('../tmp/qiutu.jpg','w') as fp:
        fp.write(img_data)


