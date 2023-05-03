import re
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

url = 'https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg3Mzc0NTA3NA==&action=getalbum&album_id=2329805780276838401#wechat_redirect'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
link = soup.find('li', {'class': 'album__list-item'}).get('data-link')
print(soup)
#访问微信推文链接
response = requests.get(link)
soup = BeautifulSoup(response.text, 'html.parser')
#lxml利用xpath分析网页（xpath = //*[@id="js_content"]/section[7]/section/section/section[2]/section）,打印出来
content = soup.find('div', {'id': 'js_content'}).get_text()
#提取文本中的zip链接，正则匹配以https://开头以.zip后缀的链接
zip_url = re.findall(r'https://.*?\.zip', content)
#打印zip链接，去除['']
print(zip_url[0])