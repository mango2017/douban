# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import logging
logger = logging.getLogger(__name__)

class RsPipeline:
    #打开数据库
    def open_spider(self,spider):
        db = spider.settings.get('MYSQL_DBNAME')
        host = spider.settings.get('MYSQL_HOST')
        port = spider.settings.get('MYSQL_PORT')
        user = spider.settings.get('MYSQL_USER')
        passwd = spider.settings.get('MYSQL_PASSWD')
        self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd)
        self.db_cur = self.db_conn.cursor()

    #关闭数据库
    def close_spider(self,spider):
        self.db_conn.commit()
        self.db_conn.close()


    #对数据库进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        logger.warning("-"*10)
        return item

    #插入数据
    def insert_db(self,item):
        values = (
            item['rs_number'],
            item['rs_name'],
            item['rs_count']
        )
        sql = 'INSERT INTO rs VALUES(null,%s,%s,%s)'

        self.db_cur.execute(sql,values)


# 完成pipelines代码后，需要在setting中设置开启
