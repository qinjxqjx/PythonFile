import requests
import re
import json
from requests.exceptions import RequestException
from multiprocessing import Pool

def get_one_page(url):
	ua = {"user-agent":"Mizilla/5.0"}

	try:
		r = requests.get(url, headers = ua)
		#print(r.text)
		if 200 == r.status_code:
			return r.text
		return None
	except RequestException:
		return None

def parse_one_page(html):
	pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
		                 +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
		                 +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
	results = re.findall(pattern, html)

	for item in results:
		yield{
			'index':item[0],
			'image':item[1],
			'title':item[2],
			'actor':item[3].strip()[3:],
			'time':item[4].strip()[5:],
			'score':item[5]+item[6],
		}

def write_to_file(content):
	with open('onepage.txt', 'a', encoding = 'utf-8') as f:
		f.write(json.dumps(content, ensure_ascii = False) + '\n')
		f.close


def main(offset):
	base_url = "http://maoyan.com/board/4?offset=" + str(offset)
	html = get_one_page(base_url)
	contents = parse_one_page(html)

	for content in contents:
		write_to_file(content)

if __name__ == '__main__':	
	# for page in range(10):
	# 	main(10 * page)
	pool = Pool()
	pool.map(main, [10 * i for i in range(10)])
	pool.close()
	pool.join()	

	