# import scrapy
# from scrapy.spiders import Spider
# from dbwang.items import DbwangItem

import scrapy
import json
import re
from scrapy import Request
from scrapy.spiders import Spider
from dbwang.items import DbwangItem

class DbwangSpiderSpider(scrapy.Spider):
    # name = 'dbwang_spider'
    # allowed_domains = ['movie.douban.com']
    # start_urls = ['https://movie.douban.com/top250']
    #
    # def parse(self, response):
    #     item = DbwangItem()
    #     movies = response.xpath('//ol[@class="grid_view"]/li')
    #     for movie in movies:
    #         item['ranking'] = movie.xpath(".//div[@class='item']//em/text()").extract_first()
    #         item['movie_name'] = movie.xpath(".//div[@class='hd']/a/span[1]/text()").extract_first()
    #         item['score'] = movie.xpath(".//div[@class='star']/span[@class='rating_num']/text()").extract_first()
    #         item['score_num'] = movie.xpath(".//div[@class='star']/span[4]/text()").extract_first()
    #         yield item
    #     next_link = response.xpath("//span[@class='next']/link/@href").extract()
    #     if next_link:
    #         next_link = next_link[0]
    #         yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)

        name = 'dbwang_spider'
        allowed_domains = ['movie.douban.com']
        # start_urls = ['http://movie.douban.com/']
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        }

        def start_requests(self):
            url = "https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20"
            yield scrapy.Request(url, headers=self.headers)

        def parse(self, response):
            datas = json.loads(response.body)
            item = DbwangItem()
            if datas:
                for data in datas:
                    item['ranking'] = data['rank']
                    item['movie_name'] = data['title']
                    item['score'] = data['score']
                    item['score_num'] = data['vote_count']
                    yield  item
                #如果datas存在数据则对下一页进行采集
                page_num = re.search(r'start=(\d+)', response.url).group(1)
                page_num = 'start=' + str(int(page_num)+20)
                next_url = re.sub(r'start=\d+', page_num, response.url)
                yield scrapy.Request(next_url,headers=self.headers)
