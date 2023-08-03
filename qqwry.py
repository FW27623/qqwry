import re
import requests
from bs4 import BeautifulSoup

def get_link(url):
    # 设置请求头，模拟浏览器访问
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,zh-TW;q=0.6',
        'Cookie': 'rewardsn=; wxtokenkey=777',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    # 访问链接并解析网页
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取微信推文链接
    link = soup.find('li', {'class': 'album__list-item js_album_item js_wx_tap_highlight wx_tap_cell'}).get('data-link')

    return link

def get_zip_url(link):
    # 访问微信推文链接并解析网页
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 提取文本中的zip链接，正则匹配以https://开头以.zip后缀的链接
    content = soup.find('div', {'id': 'js_content'}).get_text()
    zip_url = re.findall(r'https://.*?\.zip', content)

    return zip_url

if __name__ == '__main__':
    # 微信推文链接
    url = 'https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg3Mzc0NTA3NA==&action=getalbum&album_id=2329805780276838401#wechat_redirect'

    try:
        link = get_link(url)
        if link:
            zip_url = get_zip_url(link)
            if zip_url:
                # 打印zip链接，去除['']
                print(zip_url[0])
            else:
                print("没有找到zip链接")
        else:
            print("没有找到微信推文链接")
    except Exception as e:
        print("出现错误：", e)