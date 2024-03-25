import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 设置要爬取的网页 URL
url = 'https://stock.adobe.com/fr/search/images?filters%5Bcontent_type%3Aphoto%5D=1&filters%5Bcontent_type%3Aillustration%5D=1&filters%5Bcontent_type%3Azip_vector%5D=1&filters%5Bcontent_type%3Aimage%5D=1&k=visage+contente+humain&order=relevance&safe_search=1&limit=100&search_page=1&search_type=usertyped&acp=&aco=visage+contente+humain&price%5B%24%5D=1&get_facets=0'

# 发送 GET 请求并获取响应
response = requests.get(url)

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
# 找到所有图片的标签
image_tags = soup.find_all('img')

# 遍历每个图片标签，获取图片 URL 并下载
for img in image_tags:
    img_url = urljoin(url, img['src'])  # 获取图片的完整 URL
    img_name = img_url.split('/')[-1]  # 提取图片文件名
    img_path = os.path.join('../data/happy', img_name)  # 图片保存路径

    # 下载图片
    if img_name.endswith(".jpg"):
        with open(img_path, 'wb') as f:
            img_data = requests.get(img_url).content
            f.write(img_data)
        print(f"Downloaded {img_name}")

print("All images downloaded successfully!")
