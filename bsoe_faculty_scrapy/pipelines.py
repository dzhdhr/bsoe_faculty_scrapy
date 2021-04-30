# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class BsoeFacultyScrapyPipeline:
    def open_spider(self, spider):
        self.conn = pymysql.connect(
            port=3306,
            host='127.0.0.1',
            db='bsoe_faculty',
            charset='utf8',
            user='root',
            password='your password'
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        key,value = zip(*(item.items()))
        sql = 'insert into Faculty({}) values ({})'.format(
            ','.join(key),
            ','.join(['%s']*len(key))
        )
        print(sql)
        self.cursor.execute(sql,value)
        self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
        pass
