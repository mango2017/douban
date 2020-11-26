import scrapy
import logging
from rs.items import RsItem

logger = logging.getLogger(__name__)

class RsSpiderSpider(scrapy.Spider):
    name = 'rs_spider'  #爬虫名字 爬虫启动时候使用：scrapy crawl itcast
    allowed_domains = ['baidu.com'] #允许爬取的范围，防止爬虫爬到了别的网站
    # start_urls = ['https://www.baidu.com/s?wd=xpath&rsv_spt=1&rsv_iqid=0x9057622600031126&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=88093251_56_hao_pg&rsv_enter=1&rsv_dl=tb&oq=scrapy%2520%25E7%2588%25AC%25E8%2599%25AB%25E7%2599%25BE%25E5%25BA%25A6%25E7%2583%25AD%25E6%2590%259C&rsv_btype=t&inputT=2207&rsv_t=de88ER8GoD6avs2hmvh8EfNrrmGqPVrR48vpIajhRXm%2FqLxZWZNHHpf03fgV6%2Fuhr412QTzu92ES&rsv_pq=c8dd316300034634&rsv_sug2=0&rsv_sug4=2207']
    # 开始爬取的地址
    start_urls = ['https://www.baidu.com/s?wd=php&rsv_spt=1&rsv_iqid=0x9057622600031126&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=88093251_56_hao_pg&rsv_enter=1&rsv_dl=tb&oq=xpath&rsv_btype=t&inputT=724&rsv_t=1319pUuL70aYjuG1v7PA1m93QRM%2Bu0Oo68Xu8rBMhkvJcGVGsOmBM8brnq%2BYwP2JTj9HrKN%2BuWVj&rsv_pq=97e71ff300050893&rsv_sug2=0&rsv_sug4=724']


    def parse(self, response):  #数据提取方法，接收下载中间件传过来的response
        # 处理start_url地址对应的响应
        # print(response.xpath("//div[@class='opr-recommends-merge-content']//div[contains(@class,'opr-recommends-merge-item-new')]/div[@class='opr-recommends-merge-img-titleline-height']/a/text()").extract())
        # print(response.body)
        rs_list = response.xpath("//table[contains(@class,'opr-toplist1-table')]/tbody/tr")
        logger.warning(rs_list)
        for i_item in rs_list:
            rs_item = RsItem()
            rs_item['rs_name'] = i_item.xpath("./td[1]/a/text()").extract()
            rs_item['rs_name'] = rs_item['rs_name'][0].replace("\xa0", "").strip()  #去掉\n\r

            rs_item['rs_number'] = i_item.xpath('./td[1]/span[1]/text()').extract()
            rs_item['rs_number'] = rs_item['rs_number'][0].replace("\xa0", "").strip() #去掉\n\r

            rs_item['rs_count'] = i_item.xpath('./td[2]/text()').extract_first()
            yield rs_item   #将值传到pipelines.py里  返回包含选择器的列表


#extract() 返回一个包含有字符串数据的列表
#extract_first() 返回列表中的第一个字符串
# 注意：
# 1.spider中的parse方法名不能修改
# 2.需要爬取的url地址必须要属于allow_domain下的链接
# 3.response.xpath()返回的是一个含有selector对象的列表
