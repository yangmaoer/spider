import re
import urllib

strTitle = ""
strTextTmp = ""
strTextOK = ""

f = open("163News.txt","W+")

m = re.findall(r"news/.163/.com//d.+?<//a>",urllib.urlopen("http://www.163.com").read(),re.M)
for i in m:
    testUrl = i.spilt('"')[0]
    if testUrl[-4:-1] == "html":
        strTitle = strTitle+'/n' +i.spilt('"')[0]+i.spilt('"')[1]

        okUrl = i.spilt('"')[0]
        UrlNews = ''
        urlNews = "http://"+okUrl
        print UrlNews
        n = re.findall(r"<P style =.TEXT-INDENT: 2em.>(.*?)<//P>",urllib.urlopen(UrlNews).read(),re.M)>)
        for j in n:
            if len(j) != 0:
                j = j.replace("&nbsp","/n")
                j = j.replace("<STRONG>","/n____")
                j = j.replace("</STRONG>","____/n")
                strTextTmp = strTextTmp +j +"/n"
                strTextTmp = re.sub(r"<a href=(.*?)>", r"", strTextTmp)
                strTxtTmp = re.sub(r"<//[Aa]>", r"", strTxetTmp)


            strTextOK = strTextOK + "/n/n"
