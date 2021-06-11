import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'civilian'
    def start_requests(self):
        urls = [
            'http://www.thecivilian.co.nz/page/1/'
        ]
        for i in range(2, 61):
            urls.append('http://www.thecivilian.co.nz/' + 'page/' + str(i) + '/')
        custom_settings = {
            'FEED_FORMAT' : 'csv',
            'FEED_URI' : 'civilian.csv',

        }
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for products in response.css('div.inner-wrap').css('div.clearfix').css('div.recent-post').css('div.post-content'):
            yield {
                'title' : products.css('a::text').get(),
            }