import scrapy
from scrapy_splash import SplashRequest
from lxml import etree

class PetStoreSpider(scrapy.Spider):
    name = 'store'

    domain = 'https://petmarket.ua'

    start_url = 'https://petmarket.ua/aktsionnye-tovary/'

    def start_requests(self):
        yield SplashRequest(url = self.start_url, callback = self.parse)

    def parse(self, response):
        xml = etree.Element('data')
        for item in response.xpath('//ul/li[@class="catalog-grid__item"]'):
            description = item.xpath('.//div[@class="catalogCard-title"]/a/text()').extract_first().strip()
            image = item.xpath('.//img/@src').extract_first().strip()
            price = item.xpath('.//div[@class="catalogCard-price"]/text()').extract_first().strip()
            item = etree.SubElement(xml, 'item')
            etree.SubElement(item, 'description').text = description
            etree.SubElement(item, 'image').text = self.domain + image
            etree.SubElement(item, 'price').text = price
        et = etree.ElementTree(xml)
        et.write('task3_results/results.xml', encoding="UTF-8", pretty_print=True)
        yield None 



