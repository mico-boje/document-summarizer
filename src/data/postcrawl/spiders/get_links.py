import scrapy
from scrapy.spiders import CrawlSpider, Rule


class LinksSpider(scrapy.Spider):
    name = "links"
    count = 1
    link_list = []
    while count < 2000:
        link_list.append('https://www.defensenews.com/stories/air/{}/'.format(count))
        link_list.append('https://www.defensenews.com/stories/land/{}/'.format(count))
        link_list.append('https://www.defensenews.com/stories/naval/{}/'.format(count))
        count += 20
    start_urls = link_list

    def parse(self, response):
        post = response.css('div.pb-container')
        test = post.css('div.result-listing')

        for i in test:
            yield {
                'link': i.css('a::attr(href)').getall()
            }

# test = post.css('div.result-listing')
# for i in test: i.css('a::attr(href)').getall()
# for i in test: i.css('h4::text').getall()
