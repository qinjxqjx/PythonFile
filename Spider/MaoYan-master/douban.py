import re
import requests
content = requests.get("https://book.douban.com/").text
print(content)
#pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)

pattern = re.compile(r'<li.*?cover.*?href="(.*?)" title', re.S)

results = re.findall(pattern, content)


for result in results:
       url, name, author, date = result
       author = re.sub("\s", "", author)
       date = re.sub("\s", "", date)
       print(url, name, author, date)
