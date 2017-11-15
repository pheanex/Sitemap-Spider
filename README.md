# Sitemap-Spider
This is a small application as part of a coding challenge I received when I applied for a Python developer job to check my way of thinking and approach to this challenge.

## The task
> Please build an application, that is able to crawl a given website and returns its sitemap.

>Deliverables: link to public git

>Constraint: please, do not spend more than 2-3 hours on it.

## My approach / reasoning
The most idiomatic approach under the given constraints to me was to make use of an existing, easy to use python-crawling framework to do the heavy lifting. "Scrapy" seemed to match the requirements quite well and other more self-built/basic approaches like [Cartman720's version](https://github.com/Cartman720/PySitemap) appeared too laborious, although I liked the commandline-interface and output option.
Therefore I am going to use a similar command-line interface and also output-format, since it is an official standard ([Sitemap XML protocol](http://www.sitemaps.org)). Usually I'd like to write tests up front, but due to the time constraint, Scrapys nature of being a bit [cumbersome](https://doc.scrapy.org/en/latest/topics/contracts.html) to write tests for and lack of quality/reliable test-data, I decided to add the tests afterwards if enough time left, just this once :-)

## Usage
Set the website in the crawler under "start_urls" and then run the script via

```
./crawler
```
The resulting sitemap will then be stored in "sitemap.xml"

## Afterthought
I spent a lot of time getting the SiteSpider subclass to somehow dynamically accept the start_urls,
which until now I was not able to achieve. Maybe it is not really designed to be used that way?
A couple of stackoverflow questions describing the same problems may indicate that.
Nevertheless we have a working version, although still without tests and quite a few possibilities to refactor.