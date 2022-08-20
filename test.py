import requests
from bs4 import BeautifulSoup

news = requests.get("https://dantri.com.vn/the-thao.htm")
# print("https://dantri.com.vn" + link , ":" , news.status_code)
soup = BeautifulSoup(news.content, 'html.parser')
body = soup.findAll('div', class_='article-thumb')
titles = soup.findAll('h3', class_='article-title')
Dict = {}

links = [link.find('a').attrs["href"] for link in body]
imgs = [link.find('img') for link in body]
res = {links[i]: imgs[i] for i in range(len(links))}
print(res)


