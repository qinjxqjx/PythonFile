#coding=utf-8
import urllib
import re
import os

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.*?)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 1
    os.mkdir('l')
    os.chdir(os.path.join(os.getcwd(), 'l'))
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1


html = getHtml("http://tieba.baidu.com/p/3884688092")


print getImg(html)
