import scrapy
from scrapy_splash import SplashRequest
from lxml import etree

class NewsSpider(scrapy.Spider):
    name = 'news'

    visited = []

    start_url = 'https://golos.ua/news'

    def start_requests(self):
        yield SplashRequest(url = self.start_url, callback = self.parse)

    def parse(self, response):
        current_url = response.url
        self.visited.append(current_url)
        # print(response.text)
        xml = etree.Element('data')
        etree.SubElement(xml, 'page', {'url' : current_url})
        for text in response.xpath('//body//*[not(self::script) and not(self::noscript) and not(self::style)]/text()'):
            content = text.extract().strip()
            if content:
                etree.SubElement(xml, 'fragment', {'type' : 'text'}).text = content
        for image in response.xpath('//img/@src'):
            etree.SubElement(xml, 'fragment', {'type' : 'image'}).text = image.extract()
        if len(self.visited) < 20:
            pages = response.xpath('//@href')
            next_page = ''
            for page in pages:
                cur_page = page.extract()
                if not cur_page.startswith('https://golos.ua'):
                    cur_page = 'https://golos.ua' + cur_page
                if cur_page.startswith('https://golos.ua/news') and cur_page not in self.visited:
                    next_page = cur_page
                    break
            print('*\n*\n*')
            print(next_page)
            print('*\n*\n*')
            if next_page:
                yield SplashRequest(url = next_page, callback = self.parse)
        et = etree.ElementTree(xml)
        et.write('task1_results/' + str(len(self.visited)) + '.xml', encoding="UTF-8", pretty_print=True)
        yield None 

