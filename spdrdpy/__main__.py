import sys
import time
import requests
from lxml import html


def clear_screen():
	print(chr(27) + "[2J")

def speed_read(url):
	
	headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)'}
	r = requests.get(url, headers=headers)
	doc = html.fromstring(r.text)
	paragraphs = doc.xpath('//p')
	
	for p in paragraphs:
		if p.text != None:
			for word in p.text.split(' '):
				clear_screen()
				print(word)
				time.sleep(0.2)
	
if (__name__) == '__main__':
	speed_read(sys.argv[1])
