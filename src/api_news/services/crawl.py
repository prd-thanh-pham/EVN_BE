import requests
from bs4 import BeautifulSoup
from api.services import BaseService
from bs4.element import Tag
from utils.utils import Util


class CrawlService(BaseService):
    @classmethod
    def crawl_from_url(
        cls, url="https://www.evn.com.vn/c3/pages-c/Thong-tin-Su-kien-6-12.aspx"
    ):
        root_url = "https://www.evn.com.vn"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        links = soup.find_all("div", class_="row blog blog-medium")
        thumbnails = soup.find("div", class_="blog-page page_list").find_all(
            "img", class_="img-responsive"
        )
        arr_news = []
        for idx, item in enumerate(links):
            link = root_url + item.find("a").get("href")
            page_detail = requests.get(link)
            soup_detail = BeautifulSoup(page_detail.content, "html.parser")
            news = {
                "source": link,
                "title": Util.remove_space(soup_detail.find(id="ContentPlaceHolder1_ctl00_159_ltlTitle").text),
                "except": Util.remove_space(soup_detail.find('strong').text),
                "thumbnails": root_url + thumbnails[idx].get("src"),
                "content": [],
                "post_at": soup_detail.find(id='ContentPlaceHolder1_ctl00_159_lblAproved').text,
                "author": soup_detail.find(id='ContentPlaceHolder1_ctl00_159_LabelAuthor').text,
                "keyword": list(
                    map(lambda x: x.text,
                        soup_detail.find('ul', class_='list-unstyled list-inline blog-tags').find_all('a'))),
            }
            content = soup_detail.find(id="ContentPlaceHolder1_ctl00_159_FullDescirbe")
            i = 0
            item = {"title": "", "paragraph": "", "description_img": "", "image": "", "order": i}
            for child in content:
                if isinstance(child, Tag) and child.name == 'p':
                    if type(child.find('strong')) != type(None):
                        if item["title"]:
                            news["content"].append(item)
                            i = i + 1
                            item = {"title": "", "paragraph": "", "description_img": "", "image": "", "order": i}
                        item["title"] = Util.remove_space(child.text)
                    else:
                        item["paragraph"] += Util.remove_space(child.text) + "<br>"
                elif isinstance(child, Tag) and child.name == 'table':
                    item["description_img"] = Util.remove_space(child.find('td').text)
                    if type(child.find('img')) != type(None):
                        item["image"] = root_url + child.find("img").get("src")
                    news["content"].append(item)
                    i = i + 1
                    item = {"title": "", "paragraph": "", "description_img": "", "image": "", "order": i}
            if item["paragraph"]:
                news["content"].append(item)
            arr_news.append(news)
        return arr_news
