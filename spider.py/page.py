import urllib
import urllib2
import re
import time
import types
import tool
from bs4 import BeautifulSoup

class Page:
	def __init__(self):
		self.tool = tool.Tool()

	def getCurrentDate(self):
        		return time.strftime('%Y-%m-%d',time.localtime(time.time()))
    

    	def getCurrentTime(self):
        		return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))
 
    	def getPageByURL(self, url):
        	try:
            		request = urllib2.Request(url)
            		response = urllib2.urlopen(request)
            		return response.read().decode("utf-8") 
        	except urllib2.URLError, e:
        		return self.getCurrentTime(),"url error %d: %s" %(e.args[0],e.args[1])   


