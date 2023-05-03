import re
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'Cookie': 'rewardsn=; wxtokenkey=777',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
}

url = 'https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg3Mzc0NTA3NA==&action=getalbum&album_id=2329805780276838401#wechat_redirect'

#访问链接加上headers
response = requests.get(url, headers=headers)
#解析网页
soup = BeautifulSoup(response.text, 'html.parser')
<<<<<<< HEAD
#提取微信推文链接
link = soup.find('li', {'class': 'album__list-item js_album_item js_wx_tap_highlight wx_tap_cell'}).get('data-link')
=======
link = soup.find('li', {'class': 'album__list-item'}).get('data-link')
print(soup)
<<<<<<< HEAD
>>>>>>> parent of b67b5e5 (test)
=======
>>>>>>> parent of b67b5e5 (test)
#访问微信推文链接
response = requests.get(link)
soup = BeautifulSoup(response.text, 'html.parser')
#lxml利用xpath分析网页（xpath = //*[@id="js_content"]/section[7]/section/section/section[2]/section）,打印出来
content = soup.find('div', {'id': 'js_content'}).get_text()
#提取文本中的zip链接，正则匹配以https://开头以.zip后缀的链接
zip_url = re.findall(r'https://.*?\.zip', content)
#打印zip链接，去除['']
print(zip_url[0])