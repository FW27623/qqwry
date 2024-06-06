import re
import json
import requests
from bs4 import BeautifulSoup
import time

def get_link(url, retries=3, delay=5):
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,zh-TW;q=0.6',
        'Cookie': 'rewardsn=; wxtokenkey=777',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    }

    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = json.loads(response.text)
            article_list = data['getalbum_resp']['article_list']

            for article in article_list:
                title = article['title']
                if "纯真IP库社区版更新" in title:
                    link = article['url']
                    zip_url = get_zip_url(link, retries, delay)
                    if zip_url:
                        return link
            return None
        except (requests.RequestException, ValueError) as e:
            print(f"第{attempt+1}次请求失败：{e}")
            if attempt < retries - 1:
                time.sleep(delay)
    return None

def get_zip_url(link, retries=3, delay=5):
    for attempt in range(retries):
        try:
            response = requests.get(link)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            content_div = soup.find('div', {'id': 'js_content'})
            if content_div is not None:
                content = content_div.get_text()
                zip_url = re.findall(r'https://.*?\.zip', content)
                return zip_url
            else:
                return None
        except (requests.RequestException, ValueError) as e:
            print(f"第{attempt+1}次请求失败：{e}")
            if attempt < retries - 1:
                time.sleep(delay)
    return None

if __name__ == '__main__':
    url = 'https://mp.weixin.qq.com/mp/appmsgalbum?__biz=Mzg3Mzc0NTA3NA==&action=getalbum&album_id=2329805780276838401&f=json'

    try:
        link = get_link(url)
        if link:
            zip_url = get_zip_url(link)
            if zip_url:
                print(zip_url[0])
            else:
                print("没有找到zip链接")
        else:
            print("没有找到微信推文链接")
    except Exception as e:
        print("出现错误：", e)
