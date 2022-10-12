import scrapy
from ScrapyProjects.Blog.Blog.items import QuotesItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        """
        Usando XPath
        """
        print(f"Response Type >>> {type(response)}")
        rows = response.xpath("//div[@class='quote']") # Raíz do elemento

        print(f"Contagem de Quotes >> {rows.__len__()}")
        for row in rows:
            item = QuotesItem()
            item['tags'] = row.xpath('div[@class="tags"]/meta[@itemprop="keywords"]/@content').extract_firts().strip()
            item['author'] = row.xpath('//span/small[@itemprop="author"]/text()').extract_first()
            item['quote'] = row.xpath('span[@itemprop="text"]/text()').extract_first()
            item['author_link'] = row.xpath('//a[contains(@href,"/author/")]/@href').extract_first()
            if len(item['author_link']) > 0:
                item['author_link'] = 'https://quotes.toscrape.com'+item['author_link']
            yield item
