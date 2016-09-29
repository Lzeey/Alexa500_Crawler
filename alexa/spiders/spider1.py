import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from alexa.items import AlexaItem
from scrapy.selector import HtmlXPathSelector

class MySpider(CrawlSpider):
    name = 'alexaSGspider'
    allowed_domains = ['alexa.com']
    start_urls = ['http://www.alexa.com/topsites/countries/SG']

    rules = (
        # Extract links matching '/topsites/global;\d'
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('/topsites/countries;[\d]+/SG', ), restrict_xpaths=('//a[@class="next"]', )), callback='parse_item',follow= True),

    )
    
    # to extract from first page
    def parse_start_url(self, response):
        return self.parse_item(response)
        
    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        item = AlexaItem()
        item['Rank'] = response.xpath('//li[@class="site-listing"]/div[@class="count"]/text()').extract()
        tmp_name = response.xpath('//div[@class="desc-container"]/p[@class="desc-paragraph"]/a/text()').extract()
        tmp_name = [site.lower() for site in tmp_name]
        item['Name'] = tmp_name
        return item
        