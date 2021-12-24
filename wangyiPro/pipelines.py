# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class WangyiproPipeline:
    def open_spider(self,spider):
        self.fp = open('wangyi.txt','w',encoding='utf-8')

    def close_spider(self,spider):
        self.fp.close()

    def process_item(self, item, spider):
        self.fp.write(item['title'] + ':' + item['content'] + '\n')
        return item

class MysqlPipeline(object):

    def open_spider(self,spider):
        self.conn = pymysql.Connect(host = '10.10.10.1',port=3306,user='root',password='',db='spider',charset='utf8')
        self.cursor = self.conn.cursor()

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self,item,spider):
        sql = 'insert into wangyi values ("%s","%s")'  % (item['title'],item['content'])
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item
