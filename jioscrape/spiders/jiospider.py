import scrapy

class JioSpider(scrapy.Spider):
    name='jio'
    start_urls=['https://www.jiomart.com/c/groceries/fruits-vegetables/219?prod_mart_groceries_products_popularity%5Bpage%5D']

    def parse(self, response):
        for products in response.css('div.cat-item'):
            yield{
                'name': products.css('a').attrib['title'],
                'price':products.css('span[id=final_price]::text').get().replace('₹',''),
                'link': 'https://www.jiomart.com/' + products.css('a').attrib['href'],
            }

        for i in range(1,99):
            
            next_page=[f'https://www.jiomart.com/c/groceries/fruits-vegetables/219?prod_mart_groceries_products_popularity%5Bpage%5D={i}']
            url_str = ''.join(map(str, next_page))
            if url_str is not None:
                yield response.follow(url_str, callback=self.parse)

