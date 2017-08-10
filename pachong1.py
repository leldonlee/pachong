#coding=utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(http.+?.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x=0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'D:\\pythonthing\\%s.jpg' %x)
        x+=1
    return imglist

html = getHtml(r"http://www.topit.me/")

print getImg(html)

