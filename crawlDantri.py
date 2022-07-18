import requests
from bs4 import BeautifulSoup
from database import insert_data

# Crawl data from website
# danh sach các link cần crawl
listCategories = {
    'xa-hoi': 1,
    'the-thao': 2,
    'giai-tri': 3,
    'the-gioi': 4,
    'kinh-doanh': 5,
    'giao-duc-huong-nghiep': 6,
    'phap-luat': 7,
    'van-hoa': 8
}

# số bản ghi cần lấy
limit = 20

for key in listCategories:
    count = 0
    for i in range(1, 4):
        url = 'https://dantri.com.vn/' + key + '/trang-' + str(i) + '.htm'
        response = requests.get(url)
        print(url , ":" , response.status_code)
        soup = BeautifulSoup(response.content, 'html.parser')
        itemNews = soup.find_all('article', class_='article-item')
        print(soup)
        for item in itemNews:
            titles = item.findAll('h3', class_='article-title')
            links = [link.find('a').attrs["href"] for link in titles]
            try:
                for link in links:
                    news = requests.get("https://dantri.com.vn" + link)
                print("https://dantri.com.vn" + link , ":" , news.status_code)
                soup = BeautifulSoup(news.content, 'html.parser')
                title = soup.find('h1', class_='title-page').get_text()
                shotDescription = soup.find('h2', class_='singular-sapo').get_text()
                body = soup.find('div', class_='singular-content')
                htmlContent = str(body)
                print(type(htmlContent))
                content = ""
                print(htmlContent)
                try:
                    getAllTag_p = body.findChildren("p", recursive=False)
                    for tag_p in getAllTag_p:
                        content += tag_p.get_text()
                except:
                    content = ""
                if(len(content) > 100 and len(content)<3000):
                    if count < limit:
                        count += 1
                        insert_data(title, content, shotDescription, listCategories[key], htmlContent)
                    else:
                        break
            except:
                print("error")
                pass
