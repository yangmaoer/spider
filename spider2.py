
#! /usr/bin/env python
#encoding: utf-8




import re, urllib

strTitle = ""
strTxtTmp = ""
strTxtOK = ""

f = open("163News.txt", "w+")

m = re.findall(r"news\.163\.com/\d.+?<\/a>",urllib.urlopen("http://www.163.com").read(),re.M)
for i in m:
    testUrl = i.split('"')[0]
    if testUrl[-4:-1]=="html":

 
        strTitle = strTitle + "\n" + i.split('"')[0] + i.split('"')[1]


        okUrl = i.split('"')[0]
        UrlNews = ''
        UrlNews = "http://" + okUrl
       
        print UrlNews

  
        n = re.findall(r"<P style=.TEXT-INDENT: 2em.>(.*?)<\/P>",urllib.urlopen(UrlNews).read(),re.M)
        for j in n:
            if len(j) != 0:
                j = j.replace("&nbsp","\n")
                j = j.replace("<STRONG>","\n_____")
                j = j.replace("</STRONG>","_____\n")
                strTxtTmp = strTxtTmp + j + "\n"
                strTxtTmp = re.sub(r"<a href=(.*?)>", r"", strTxtTmp)
                strTxtTmp = re.sub(r"<\/[Aa]>", r"", strTxtTmp)

   
        strTxtOK = strTxtOK + "\n\n\n===============" + i.split('"')[0] + i.split('"')[1] + "===============\n" + strTxtTmp
        strTxtTmp = ""
        print strTxtOK

f.write(strTitle + "\n\n\n" + strTxtOK)
f.close()
