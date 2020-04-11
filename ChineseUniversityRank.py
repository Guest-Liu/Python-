#!/usr/bin/python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import bs4

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return" "

def fillUinvList1(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])

def printUnivList1(ulist, num):
    tplt = "{0:^5}\t\t{1:^10}\t\t\t\t{2:^5}"
    print(tplt.format("排名","学校名称","省份"))
    print(tplt.format("====","========","===="))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2]))

def main():
    uinfo = [ ]
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUinvList1(uinfo, html)
    printUnivList1(uinfo, 30) # 30 univs
main()















    
