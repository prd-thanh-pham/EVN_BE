import requests
from bs4 import BeautifulSoup
from api.services import BaseService
from utils.utils import Util
import functools


class CrawlService(BaseService):
    @classmethod
    def crawl(cls, url):
        url = url
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        hot_new = soup.find('div', class_='item').find('a')
        titles = [hot_new.get('title')]
        links = [hot_new.get('href')]
        new_feeds = soup.find_all('h3', class_='title-news13 mt5')
        for i in new_feeds:
            a = i.find('a')
            titles.append(a.get('title'))
            links.append((a.get('href')))
        arr_news = []
        for item in links:
            page_detail = requests.get(url + item)
            soup_detail = BeautifulSoup(page_detail.content, 'html.parser')
            news = {
                "source": url + item,
                "title": Util.remove_space(soup_detail.find(id="ContentPlaceHolder1_ctl00_159_ltlTitle").text),
                "gists": list(map(lambda x: Util.remove_space(x.text), soup_detail.find_all('strong'))),
                "except": Util.remove_space(soup_detail.find('strong').text),
                "post_at": soup_detail.find(id='ContentPlaceHolder1_ctl00_159_lblAproved').text,
                "author": soup_detail.find(id='ContentPlaceHolder1_ctl00_159_LabelAuthor').text
            }
            body = soup_detail.find('div', class_='col-lg-12 col-md-12 col-sm-12 col-xs-12')
            paragraph = soup_detail.find_all('p', style="text-align:justify")
            # news["contents"] = list(map(lambda x: Util.remove_space(x.text), paragraph))
            news["content"] = '<br>'.join(list(map(lambda x: Util.remove_space(x.text), paragraph)))
            news["images"] = []
            images = soup_detail.select('tbody tr td')
            for img in images:
                image = {"title": Util.remove_space(img.text)}
                if type(img.find("img")) != type(None):
                    image["src"] = img.find("img").get("src")
                news["images"].append(image)
            arr_news.append(news)
        return arr_news
