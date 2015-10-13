#coding=utf-8
'''
use this moudle to crawl the title and content links
'''
from karlspider.items import DmozItem
from scrapy.selector import HtmlXPathSelector
from karlspider.data_manage.data_option import DataOptionSave,DataOptionGet
'''
crawl the content's link and content's title from tencent chinanews 
save the content's link and title in database
'''
def Crawl_China_Title(response):
    _title = []
    _link = []
    item = DmozItem()
    hxs = HtmlXPathSelector(response)
    sites = hxs.select('//a')
    dataOptionGet = DataOptionGet()
    latest_link = dataOptionGet.get_Last_Link_CH()
    for site in sites:
        item['title'] = site.select("//a[@target='_blank' and @class='linkto']/text()").extract()
        item['link'] = site.select("//a[@target='_blank' and @class='linkto']/@href").extract()
        break
    for i in range(len(item['title'])):
        if "http://news.qq.com"+str(item['link'][i]) == latest_link:
            break
        _title.append(item['title'][i])
        _link.append(item['link'][i])
    if len(_link) > 0:
        dataOptionSave = DataOptionSave()
        dataOptionSave.Chnews_Title_Save(str(_link), str(_title))

'''
crawl the content's link and content's title from tencent internationalnews 
save the content's link and title in database
'''
def Crawl_Inter_Title(response):
    _title = []
    _link = []
    item = DmozItem()
    hxs = HtmlXPathSelector(response)
    sites = hxs.select('//a')
    dataOptionGet = DataOptionGet()
    latest_link = dataOptionGet.get_Last_Link_IN()
    for site in sites:
        item['title'] = site.select("//a[@target='_blank' and @class='linkto']/text()").extract()
        item['link'] = site.select("//a[@target='_blank' and @class='linkto']/@href").extract()
        break
    for i in range(len(item['title'])):
        if "http://news.qq.com"+str(item['link'][i]) == latest_link:
            break
        _title.append(item['title'][i])
        _link.append(item['link'][i])
    if len(_link) > 0:
        dataOptionSave = DataOptionSave()
        dataOptionSave.Inter_Title_Save(str(_link), str(_title))

'''
this method crawl the joke from budejie

first select all the tag <p> 
then select all the content which tag is <p> and tag's element is "class='web_size'"

save the content in a list
convert the list into string

save the string in database

'''
def Crawl_Joke_Content(response):
    dataOptionSave = DataOptionSave()
    jokecontent = []
    item = DmozItem()
    hxs = HtmlXPathSelector(response)
    sites = hxs.select('//p')
    for site in sites:
        item['desc'] = site.select("//p[@class='web_size']").extract()
    for i in range(len(item['desc'])):
        jokecontent.append(item['desc'][i])
    jokecontent = str(jokecontent)
    dataOptionSave.Joke_Save(jokecontent)
    jokecontent = eval(jokecontent)

'''
use this method to crawl information from tencent
first select all tag <div>
then select the <div> which element is "id='Cnt-Article-QQ'"

save the information in a list
convert the list into a string
save the string in database
'''
def Crawl_China_Content(response):
    newscontent = []
    hxs = HtmlXPathSelector(response)
    title = hxs.select("//h1/text()")[0].extract()
    sites = hxs.select("//div")
    divs = sites.select("//div[@id=\"Cnt-Main-Article-QQ\"]")
    for p in divs[0].select(".//p"): # extracts all <p> inside
        newscontent.append(p.extract())
    newscontent = str(newscontent)
    dataOptionSave = DataOptionSave()
    dataOptionSave.Chnews_Content_Save(title, newscontent)

'''
use this method to crawl information from tencent
first select all tag <div>
then select the <div> which element is "id='Cnt-Article-QQ'"

save the information in a list
convert the list into a string
save the string in database
'''
def Crawl_Inter_Content(response):
    newscontent = []
    hxs = HtmlXPathSelector(response)
    title = hxs.select("//h1/text()")[0].extract()
    sites = hxs.select("//div")
    divs = sites.select("//div[@id=\"Cnt-Main-Article-QQ\"]")
    for p in divs[0].select(".//p"): # extracts all <p> inside
        newscontent.append(p.extract())
    newscontent = str(newscontent)
    dataOptionSave = DataOptionSave()
    dataOptionSave.Inter_Content_Save(title, newscontent)

'''
crawl the titles and links from fenghuang community
save the titles and links in database
'''
def Crawl_Community_Title(response):
    _title = []
    _link = []
    item = DmozItem()
    hxs = HtmlXPathSelector(response)
    item['title'] = hxs.select("//div[@class=\"newsList\"]//ul//li//a/text()").extract()
    item['link'] = hxs.select("//div[@class=\"newsList\"]//ul//li//a/@href").extract()
    dataOptionGet = DataOptionGet()
    latest_link = dataOptionGet.get_Last_Link_CO()
    for i in range(len(item['title'])):
        if str(item['link'][i]) == latest_link:
            break
        _title.append(item['title'][i])
        _link.append(item['link'][i])
    if len(_link) > 0:
        dataOptionSave = DataOptionSave()
        dataOptionSave.Comu_Title_Save(_link,_title) 

'''
crawl the community content from fenghuang community

first crawl all the tag <div>
the select the <div> which element is id="main_content"
'''
def Crawl_Community_Content(response):
    newscontent = []
    hxs = HtmlXPathSelector(response)
    title = hxs.select("//h1/text()")[0].extract()
    sites = hxs.select("//div")
    divs = sites.select("//div[@id=\"main_content\" and @class=\"js_selection_area\"]")
    try:
        for p in divs[0].select(".//p"): # extracts all <p> inside
            newscontent.append(p.extract())
        newscontent = str(newscontent)
        dataOptionSave = DataOptionSave()
        dataOptionSave.Comu_Content_Save(title, newscontent)
    except:
        pass
    
'''
crawl title military news titles and links from sina
save the titles and links in database
'''
def Crawl_Malitary_Title(response):
    _title = []
    _link = []
    item = DmozItem()
    hxs = HtmlXPathSelector(response)
    item['title'] = hxs.select("//div[@class='dd_bt']//a/text()").extract()
    item['link'] = hxs.select("//div[@class='dd_bt']//a/@href").extract()
    dataOptionGet = DataOptionGet()
    latest_link = dataOptionGet.get_Last_Link_MA()
    for i in range(len(item['title'])):
        if "http://www.chinanews.com"+str(item['link'][i]) == latest_link:
            break
        _title.append(item['title'][i])
        _link.append(item['link'][i])
    if len(_link) > 0:
        dataOptionSave = DataOptionSave()
        dataOptionSave.Mali_Title_Save(_link,_title) 

'''
crawl the military contents from sina
select all tag <div> from sina
select all tag <div> which elements are class='blkContainerSblkCon' and id='artibody'
select all tag <p> from <div>
save the content in a list
convert the list into string 
save the string in database
'''        
def Crawl_Malitary_Content(response):
    newscontent = []
    hxs = HtmlXPathSelector(response)
    title = hxs.select("//title/text()")[0].extract()
    title = title.split('-')[0]
    sites = hxs.select("//div")
    divs = sites.select("//div[@class=\"left_zw\"]")
    try:
        for p in divs[0].select(".//p"): # extracts all <p> inside
            newscontent.append(p.extract())
        newscontent = str(newscontent)
        dataOptionSave = DataOptionSave()
        dataOptionSave.Mali_Content_Save(title, newscontent)
    except:
        pass
'''
crawl the Sports News's titles and links from http://www.chinanews.com
'''
def Crawl_Sport_Title(response):
    _title = []
    _link = []
    item = DmozItem()
    hxs = HtmlXPathSelector(response)
    item['title'] = hxs.select("//div[@class='dd_bt']//a/text()").extract()
    item['link'] = hxs.select("//div[@class='dd_bt']//a/@href").extract()
    dataOptionGet = DataOptionGet()
    latest_link = dataOptionGet.get_Last_Link_Sport()
    for i in range(len(item['title'])):
        if "http://www.chinanews.com"+str(item['link'][i]) == latest_link:
            break
        _title.append(item['title'][i])
        _link.append(item['link'][i])
    if len(_link) > 0:
        dataOptionSave = DataOptionSave()
        dataOptionSave.Sport_Title_Save(_link,_title)    

'''
crawl the Sports News from http://www.chinanews.com
'''
def Crawl_Sport_Content(response):
    newscontent = []
    hxs = HtmlXPathSelector(response)
    title = hxs.select("//title/text()")[0].extract()
    title = title.split('-')[0]
    sites = hxs.select("//div")
    divs = sites.select("//div[@class=\"left_zw\"]")
    for p in divs[0].select(".//p"): # extracts all <p> inside
        newscontent.append(p.extract())
    newscontent = str(newscontent)
    dataOptionSave = DataOptionSave()
    dataOptionSave.Sport_Content_Save(title, newscontent)
    
'''
Crawl Entertainment from sina
'''    
def Crawl_Entertainment_Title(response):
    _title = []
    _link = []
    item = DmozItem()
    hxs = HtmlXPathSelector(response)
    item['title'] = hxs.select("//div[@class=\"news-item  img-news-item\"]//h2//a/text()").extract()
    item['link'] = hxs.select("//div[@class=\"news-item  img-news-item\"]//h2//a/@href").extract()
    dataOptionGet = DataOptionGet()
    latest_link = dataOptionGet.get_Last_Link_ET()
    for i in range(len(item['title'])):
        if str(item['link'][i]) == latest_link:
            break
        _title.append(item['title'][i])
        _link.append(item['link'][i])
    if len(_link) > 0:
        dataOptionSave = DataOptionSave()
        dataOptionSave.Entertainment_Title_Save(_link,_title) 
    
'''
crawl the 
'''
def Crawl_Entertainment_Content(response):
    newscontent = []
    hxs = HtmlXPathSelector(response)
    title = hxs.select("//title/text()")[0].extract()
    title = title.split('|')[0]
    sites = hxs.select("//div")
    try:
        divs = sites.select("//div[@class=\"blkContainerSblkCon BSHARE_POP clearfix\" and @id=\"artibody\"]")
        for p in divs[0].select(".//p"): # extracts all <p> inside
            newscontent.append(p.extract())
        newscontent = str(newscontent)
        dataOptionSave = DataOptionSave()
        dataOptionSave.Entertainment_Content_Save(title, newscontent)
    except:
        pass
