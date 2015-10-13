#! /usr/bin/env python 
#encoding: utf-8
import urllib2
from bs4 import BeautifulSoup
import re,os,sys
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p></html>
# """
def main(self):
	f_handler = open("out.log","w")
	sys.stdout = f_handler
	page = open("page.txt",'r')
	content = page.readline()
	start_page = int(content.strip())-1
	page.close()
	print self.ge
	

		

src = 'http://news.163.com'
request = urllib2.Request(src)
# request = urllib2.Request('http://news.163.com/15/1011/00/B5JV8ISA00014AEE.html')
response = urllib2.urlopen(request)
html = response.read()
#rex = r'src = "http://(.*).jpg"'
#lists = re.findall(rex,html)
soup = BeautifulSoup(html)
html_index = soup.find_all('a',href = re.compile("http://news.163.com/15/"))
for i in html_index:
	# str = 'news.163'
	# # print type(i)

	# if str in repr(i):
	# 	# pattern = re.compile(r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?') 
	# 	pattern = re.compile(r'(http|ftp|https):\/\/[.*]+(\.[\w\-_]+)+(html|htm)')
	# 	tmp = re.search(pattern,repr(i))
	# 	if tmp:
	# 		print tmp.group()
	# 	else:
	# 		print 'error'
	pattern = re.compile(r"(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?")
	tmp = re.search(pattern,repr(i))
	if tmp:

