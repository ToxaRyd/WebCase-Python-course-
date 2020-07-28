from bs4 import BeautifulSoup
import requests
import re

titles = []
urls = []
url = 'https://overreacted.io'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
c = 0

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, features="html.parser")
for i in soup.findAll('h3'):
	titles.append(i.get_text().strip())
	urls.append(i.find('a').get('href'))

with open('2nd_week_task_answers.txt', 'w') as f:
	for i in titles:
		f.write(f'{i} - {url}{urls[c]}\n')
		c+=1
