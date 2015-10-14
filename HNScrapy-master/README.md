HNScrapy
========

Hacker News Crawler based upon Scrapy which crawls the entire site and stores the links in the Database.

Steps to Install
========

1. Git clone the repository into your local system.
2. Install Scrapy via **pip**.

        $ pip install scrapy
        
3. Configure Database settings in **settings.py**
4. Run the crawler by this command.  

        $ scrapy crawl hn
        
Extras
========

Output the data in **JSON** format by this command

    scrapy crawl hn -o items.json -t json

Dependencies
========

1. BeautifulSoup
2. Lxml
3. OpenSSL

Tutorial
========

Read the [tutorial](http://pypix.com/python/build-website-crawler-based-upon-scrapy/)
 for detailed explanations.
