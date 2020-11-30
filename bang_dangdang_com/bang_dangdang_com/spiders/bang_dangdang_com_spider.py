import scrapy
import re
from scrapy import cmdline
#scrapy crawl bang_dangdang_com_spider -o test.json 生成json文件
class BangDangdangComSpiderSpider(scrapy.Spider):
    name = 'bang_dangdang_com_spider'
    allowed_domains = ['bang.dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1']

    def parse(self, response):
        book_list = response.xpath("//ul[@class='bang_list clearfix bang_list_mode']/li")
        for i_item in book_list:
            book_item = {}
            book_item['list_num red'] = i_item.xpath("./div[1]/text()").extract_first() #排名
            book_item['pic'] = i_item.xpath("./div[@class='pic']/a/img/@src").extract_first()  #图片地址
            book_item['name'] = i_item.xpath("./div[@class='name']/a/text()").extract_first() #书名
            book_item['tuijian'] = i_item.xpath("./div[@class='star']//span[@class='tuijian']/text()").extract_first() #推荐指数
            book_item['biaosheng'] = i_item.xpath("./div[@class='biaosheng']//span/text()").extract_first()  #五星评分次数
            book_item['price'] = i_item.xpath("./div[@class='price']/p//span[@class='price_n']/text()").extract_first()  #价格
            book_item['publisher_info'] = i_item.xpath("./div[@class='publisher_info']/a/@title").extract_first()  #作者
            # print(book_item)
            yield book_item
        next_link = response.xpath("//div[@class='paginating']//li[@class='next']/a/@href").extract()
        if next_link:
            next_link = next_link[0]
            p1 = re.compile(r"['](.*?)[']", re.S)  # 最小匹配
            page = re.findall(p1, next_link)
            next_url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"+page[0]
            print(next_url)
            yield scrapy.Request(next_url,callback=self.parse)





