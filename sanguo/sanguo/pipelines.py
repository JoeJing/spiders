# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
import sanguo.items
import scrapy.exceptions


class SanguoPipeline(object):
    def open_spider(self, spider):
        self.conn = mysql.connector.connect(host=sanguo.settings.MYSQL_HOST, port=sanguo.settings.MYSQL_PORT, user=sanguo.settings.MYSQL_USER,
                                            password=sanguo.settings.MYSQL_PASSWORD, database=sanguo.settings.MYSQL_DB)
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

    def process_item(self, item, spider):
        try:
            sql = "select 1 from sanguo_renwu where id = '%s' ;" % item['id']
            self.cursor.execute(sql)
            self.cursor.fetchall()
            if self.cursor.rowcount <= 0:
                sql = "insert into `spider_db`.`sanguo_renwu` ( `id`, `name`, `zi`, `pic`, `pinyin`, `sex`, `zhengshi`, `shengsi`, `jiguan`, `content`, `cata`) \
                       values ( '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
                      (item['id'], item['name'], item['zi'], item['pic'], item['pinyin'], item['sex'], item['zhengshi'], item['shengsi'], item['jiguan'], item['content'], item['cata'])
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            # 发生错误时回滚
            self.conn.rollback()
        finally:
            raise scrapy.exceptions.DropItem()
