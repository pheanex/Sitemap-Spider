#!/usr/bin/env python
from scrapy.crawler import CrawlerProcess
from scrapy.spider import Rule
from scrapy.spiders import CrawlSpider
from scrapy.linkextractors import LinkExtractor
import argparse

parser = argparse.ArgumentParser(description="Sitemap generator")
parser.add_argument('--url', action="store", default="",
                    help="The URL to start crawling from (also limited to this domain)")
parser.add_argument('--output', action="store", default="sitemap.xml", help="The file path to write the sitemap to")
args = parser.parse_args()

found_urls = set()


class SitemapScraper(CrawlSpider):
    name = 'SitemapSpider'
    allowed_domains = ['rewe-digital.com']
    start_urls = ['https://rewe-digital.com']

    rules = [
        Rule(LinkExtractor(allow_domains=allowed_domains, unique=True), callback='parse_item', follow=True)
    ]

    @staticmethod
    def parse_item(response):
        found_urls.add(response.url)
        return response.request


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(SitemapScraper)
process.start()
