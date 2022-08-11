import scrapy


class AuthorsSpider(scrapy.Spider):
    name = 'authors'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):            
            yield {
                'keywords': quote.xpath("div[@class='tags']/a/text()").extract(),
                'author': quote.xpath("span/small/text()").extract(),
                'quote': quote.xpath("span[@class='text']/text()").get()
                }
            
