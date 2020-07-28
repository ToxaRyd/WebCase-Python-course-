from bs4 import BeautifulSoup
import requests
import re

count = 1
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
url = 'https://flaviocopes.com/'

def  url_find(soup):
	txtlink = i.find('a').get('href')
	return txtlink

def url_getText(url):
	ar = requests.get(url, headers=headers)
	souptxt = BeautifulSoup(ar.text, features="html.parser")
	txt = souptxt.find('div', attrs={'class': 'post-content clearfix'}).getText()
	name = souptxt.find('h1').get_text().strip()
	return name, txt

with open('SiteParsing.txt', 'w', encoding=('utf8')) as f:
	pass

while True:
	try:
		r = requests.get(url, headers=headers)
		soup = BeautifulSoup(r.text, features="html.parser")
		for i in soup.findAll('li'):
			try:
				a = url_getText(url_find(i))
				with open('SiteParsing.txt', 'a', encoding=('utf8')) as f:
					f.write(a[0])
					f.write(a[1])
					f.write('*'*150)
					f.write('\n')
			except:
				pass
		count += 1
		url = f'https://flaviocopes.com/page/page/{count}/'
	except:
		print('Site has been parsed!')
		break