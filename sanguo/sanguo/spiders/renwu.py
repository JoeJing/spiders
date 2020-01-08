# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.selector import Selector
import demjson
import sanguo.items


# scrapy crawl renwu
class RenwuSpider(scrapy.Spider):
    name = 'renwu'
    allowed_domains = ['e3ol.com']
    start_urls = ['http://www.e3ol.com/biography-index.html']

    def start_requests(self):
        for i in range(225):
            yield Request("http://www.e3ol.com/biography/inc_ajax.asp?types=index&a1=&a2=&a3=&a4=&a7=&a6=&a5=&key=&pageno={0}".format(i+1))

    def parse(self, response):
        json_text = str(''.join(Selector(response=response).xpath('/html/body/p/text()').extract())).strip('(').strip(')')
        text = demjson.decode(json_text)
        for item in text['soul']:
            renwu = sanguo.items.SanguoItem()
            renwu['id'] = item['id']
            renwu['name'] = item['name']
            renwu['zi'] = item['zi'].replace('字：', '')
            renwu['pic'] = item['pic']
            renwu['pinyin'] = item['pinyin']
            renwu['sex'] = item['sex']
            renwu['zhengshi'] = item['zhengshi']
            renwu['shengsi'] = item['shengsi'].replace('\xa0 ', '')
            renwu['jiguan'] = item['jiguan'].replace('\xa0 籍贯：', '')
            renwu['content'] = item['content']
            renwu['cata'] = item['cata'].replace('主效：', '')
            yield renwu


