#coding=utf-8
#下载贴吧中图片
import urllib
import re
import os
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg=r'<img class="BDE_Image" .*?src="(.+?\.jpg)" '
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 1
    #dir = 'C:\Users\Administrator\Desktop\img'
    os.mkdir('pictures')
    
    dir = './pictures'
    
    for imgurl in imglist:
        picname=str(x) + '.jpg'
        filename = os.path.join(dir,picname)
        urllib.urlretrieve(imgurl,filename)
        x+=1


html = getHtml("http://tieba.baidu.com/p/4804755311?see_lz=1")

print getImg(html)
os.system("pause")
