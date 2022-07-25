# -*- coding: utf-8 -*-
# Ref : https://www.cloudsigma.com/how-to-crawl-a-web-page-with-scrapy-and-python-3/
import scrapy # scrapy runspider cloudsigma_spider.py

class CloudSigmaCrawler(scrapy.Spider):
    name = "cloudsigma_crawler"
    start_urls = ['https://www.cloudsigma.com/blog']

    custom_settings = {'FEED_URI': "./examples/cloudsigma_%(time)s.csv"
                    , 'FEED_FORMAT': 'csv'}
    # custom_settings = {'FEED_URI': "./examples/cloudsigma_%(time)s.json"
    #                 , 'FEED_FORMAT': 'json'}

    def parse(self, response):
        SET_SELECTOR = '.post'
        for tutorial in response.css(SET_SELECTOR):
            NAME_SELECTOR = '.entry-wrap .entry-header > h2 > a ::text'
            URL_SELECTOR = '.entry-featured > a ::attr(href)'
            IMG_SELECTOR = 'img ::attr(data-lazy-src)'
            CAPTION_SELECTOR = '.entry-content > p::text'
            yield {
                'title': tutorial.css(NAME_SELECTOR).extract_first(),
                'image': tutorial.css(IMG_SELECTOR).extract_first(),
                'url': tutorial.css(URL_SELECTOR).extract_first(),
                'caption': tutorial.css(CAPTION_SELECTOR).extract_first(),
            }

        NEXT_PAGE_SELECTOR = '.x-pagination > ul.center-list > li > a.prev-next::attr("href")'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page[-1]),
                callback=self.parse
            )