import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'fortune'
    def start_requests(self):
        urls = [
            'https://fortune.com/tag/coronavirus/page/1/'
        ]
        for i in range(2, 260):
            urls.append('https://fortune.com/tag/coronavirus/page/'+ str(i) + '/')
        
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for products in response.css('div.termArchiveWrapper__wrapper--Hd2x5').css('div.termArchiveWrapper__flexContainer--2_Mrc').css(
                    'li.termArchiveContentList__item--1LvxK').css('div.termArchiveContentListItem__wrapper--1mGkD').css('div.termArchiveContentListItem__card--1he95').css(
                        'div.termArchiveContentListItem__title--14jcP').css('a'):
            yield {
                'title' : products.css('div::text').get(),
            }