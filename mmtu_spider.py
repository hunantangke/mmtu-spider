import requests
from bs4 import BeautifulSoup


all_url = 'http://www.mzitu.com/all'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
start_html = requests.get(all_url, headers=headers)

soup = BeautifulSoup(start_html.text, 'lxml')
all_a = soup.find('div', class_='all').find_all('a')

for a in all_a:
    title = a.get_text()
    href = a['href']
    html = requests.get(href, headers=headers)
    soup_a = BeautifulSoup(html.text, 'lxml')
    max_span = soup_a.find('div', class_='pagenavi').find_all(
        'span')[-2].get_text()

    for page in range(1, int(max_span) + 1):
        page_url = href + '/' + str(page)
        img_html = requests.get(page_url, headers=headers)
        soup_img = BeautifulSoup(img_html.text, 'lxml')
        img_url = soup_img.find('div', class_='main-image').find('img')['src']
        name = img_url[-9:-4]
        img = requests.get(img_url, headers=headers)
        f = open(name + '.jpg', 'ab')  # 媒体文件要加上b
        f.write(img.content)
        f.close()
