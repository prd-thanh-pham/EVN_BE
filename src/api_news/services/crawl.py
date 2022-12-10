import requests
from bs4 import BeautifulSoup
from django.db import transaction
from api.services import BaseService
from bs4.element import Tag
from api_news.models import Topic, News, Content, Keyword
from .news import NewsService
from .content import ContentService
from .keyword import KeywordService
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
                "title": Util.remove_space(
                    soup_detail.find(id="ContentPlaceHolder1_ctl00_159_ltlTitle").text
                ),
                "excerpt": Util.remove_space(soup_detail.find("strong").text),
                "thumbnail": root_url + thumbnails[idx].get("src"),
                "content": [],
                "post_at": soup_detail.find(
                    id="ContentPlaceHolder1_ctl00_159_lblAproved"
                ).text,
                "author": soup_detail.find(
                    id="ContentPlaceHolder1_ctl00_159_LabelAuthor"
                ).text,
                "keyword": list(
                    map(
                        lambda x: x.text,
                        soup_detail.find(
                            "ul", class_="list-unstyled list-inline blog-tags"
                        ).find_all("a"),
                    )
                ),
            }
            content = soup_detail.find(id="ContentPlaceHolder1_ctl00_159_FullDescirbe")
            i = 0
            item = {
                "title": "",
                "paragraph": "",
                "description_img": "",
                "image": "",
                "order": i,
            }
            for child in content:
                if isinstance(child, Tag) and child.name == "p":
                    if type(child.find("strong")) != type(None):
                        if item["title"]:
                            news["content"].append(item)
                            i = i + 1
                            item = {
                                "title": "",
                                "paragraph": "",
                                "description_img": "",
                                "image": "",
                                "order": i,
                            }
                        item["title"] = Util.remove_space(child.text)
                    else:
                        item["paragraph"] += Util.remove_space(child.text) + "<br>"
                elif isinstance(child, Tag) and child.name == "table":
                    item["description_img"] = Util.remove_space(child.find("td").text)
                    if type(child.find("img")) != type(None):
                        item["image"] = root_url + child.find("img").get("src")
                    news["content"].append(item)
                    i = i + 1
                    item = {
                        "title": "",
                        "paragraph": "",
                        "description_img": "",
                        "image": "",
                        "order": i,
                    }
            if item["paragraph"]:
                news["content"].append(item)
            arr_news.append(news)
        return arr_news

    @classmethod
    def thread_crawl(cls):
        list_topic = Topic.objects.all()
        for topic in list_topic:
            print("Crawl in url ", topic.source)
            data = CrawlService.crawl_from_url(topic.source)
            try:
                with transaction.atomic():
                    data, news_data = NewsService.create_list_news(data, topic)
                    news_objs = News.objects.bulk_create(
                        news_data, ignore_conflicts=True
                    )
                    content_data = ContentService.create_list_content(data, news_objs)
                    keyword_data = KeywordService.create_list_keyword(data, news_objs)
                    Content.objects.bulk_create(content_data, ignore_conflicts=True)
                    Keyword.objects.bulk_create(keyword_data, ignore_conflicts=True)
            except Exception as e:
                print("Error: ", e)
        print("Crawl finished")
