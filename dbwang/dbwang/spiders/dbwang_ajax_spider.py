import scrapy
import json
from scrapy import Request
from scrapy.spiders import Spider
from dbwang.items import DbwangItem

class DbwangAjaxSpiderSpider(scrapy.Spider):
    name = 'dbwang_ajax_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"
        yield  scrapy.Request(url,headers=self.headers)

    def parse(self, response):
        datas = json.load(response.body)
        item = DbwangItem()
        print(datas)
