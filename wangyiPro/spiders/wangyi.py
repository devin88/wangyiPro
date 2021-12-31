import scrapy
from wangyiPro.items import WangyiproItem
from selenium import webdriver
import platform
import sys,os

#dfdfdfdf
#test2
#test45
class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    #allowed_domains = ['www.163.com']
    start_urls = ['https://push2.eastmoney.com/api/qt/ulist.np/get?fltt=2&invt=2&fields=f2,f3,f12,f14,f9&cb=jQuery183049534260854690526_1640907252730&ut=267f9ad526dbe6b0262ab19316f5a25b&secids=1.688200,0.300450,1.601225,1.600438,0.300037,0.300390,1.603906,1.600188,1.603260,0.002756,&_=1640907253735']
    model_urls = []
    osversion=platform.system()
    project_path = os.path.dirname(os.path.abspath(__file__))

    if osversion == 'Windows':
        driver = webdriver.Chrome(executable_path = project_path + r'.\tools\windows\chromedriver.exe')
    elif osversion == 'Darwin':
        driver = webdriver.Chrome(executable_path =  project_path + r'/tools/mac/chromedriver')
        print(driver)
        #driver = webdriver.Chrome(executable_path =  r'/Users/jidi/ops/wangyiPro/wangyiPro/spiders/tools/mac/chromedriver')
    elif osversion == 'Linux':
        driver = webdriver.Chrome(executable_path = project_path + r'/tools/linux/chromedriver')
    else:
        sys.exit()

    def parse(self,response):
        #urls = ['http://fundf10.eastmoney.com/ccmx_006230.html']
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse_check)

    def parse_check(self,response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
'''
    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        index = [2,3,5,6,8]
        for i in index:
            model_url = li_list[i].xpath('./a/@href').extract_first()
            self.model_urls.append(model_url)
        for url in self.model_urls:
            yield scrapy.Request(url=url,callback=self.parse_model)

    def parse_model(self,response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
            if detail_url:
                item = WangyiproItem()
                item['title'] = title
                yield scrapy.Request(url=detail_url,callback=self.parse_detail,meta={'item': item})

    def parse_detail(self,response):
        #content = response.xpath('//*[@id="endText"]/p/text()').extract()
        content = response.xpath('//*[@class="post_body"]/p/text()').extract()
        content = '\n'.join(content)

        item = response.meta['item']
        item['content'] = content
        yield item

    def closed(self,reason):
        self.driver.quit()
'''


