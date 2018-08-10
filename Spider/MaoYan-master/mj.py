import requests
from requests.exceptions import RequestException
import re
import json

def get_one_page_text(url):
    kv = {"user-agent": "Mizilla/5.0"}

    try:
        response = requests.get(url, headers=kv)
        #print(response.text)

        if 200 == response.status_code:
            return response.text
        return None
    except RequestException:
        return None

def parse_html(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern, html)
    print(items)

    for item in items:
        yield {
            'index':item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

def write_to_file(content):
    with open('resu.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page_text(url)

    for item in parse_html(html):
        print(item)
        write_to_file(item)


if __name__ == "__main__":
    for i in range(10):
        main(i*10)
