import  requests
import re
import os
if __name__ == "__main__":
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    url = 'https://www.qiushibaike.com/pic/page/%d/?s=5184961'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
    }

    #使用通用爬虫对url
    for pageNum in range(1,36):
        new_url = format(url%pageNum)
        page_text = requests.get(url=new_url,headers=headers).text

        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex,page_text,re.S)

        for src in img_src_list:
            #拼出完整的图片url
            src= 'https:' +src
            #请求二进制数据
            img_data = requests.get(url=src,headers=headers).content
            #生成图片名称
            imag_name = src.split('/')[-1]
            #设置图片路径
            imgPath = './qiutuLibs/' + imag_name
            with open(imgPath,'wb') as fp:    #写入二进制数据，因此用wb
                fp.write(img_data)
                print(img_name,'下载成功!!!')