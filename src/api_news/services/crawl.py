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
            content = soup_detail.find(id="ContentPlaceHolder1_ctl00_159_FullDescirbe")
            news = {
                "title": soup_detail.find(
                    id="ContentPlaceHolder1_ctl00_159_ltlTitle"
                ).text,
                "post_at": soup_detail.find(
                    id="ContentPlaceHolder1_ctl00_159_lblAproved"
                ).text,
                "thumbnail": root_url + thumbnails[idx].get("src"),
                "source": link,
                "author": soup_detail.find(
                    id="ContentPlaceHolder1_ctl00_159_LabelAuthor"
                ).text,
                "excerpt": Util.remove_space(soup_detail.find("strong").text),
                "gists": list(
                    map(
                        lambda x: Util.remove_space(x.text),
                        soup_detail.find_all("strong"),
                    )
                ),
                "content": [],
                "keyword": list(
                    map(
                        lambda x: x.text,
                        soup_detail.find(
                            "ul", class_="list-unstyled list-inline blog-tags"
                        ).find_all("a"),
                    )
                ),
                "image": [],
            }
            p = ""
            i = 0
            for _idx, child in enumerate(content):
                if isinstance(child, Tag) and child.name == "p":
                    p += Util.remove_space(child.text) + "<br>"
                elif isinstance(child, Tag) and child.name == "table":
                    news["content"].append({"paragraph": p, "order": i})
                    image = {
                        "title": Util.remove_space(child.find("td").text),
                        "order": i,
                    }
                    if type(child.find("img")) != type(None):
                        image["src"] = root_url + child.find("img").get("src")
                    news["image"].append(image)
                    p = ""
                    i = i + 1
            if p:
                news["content"].append({"paragraph": p, "order": i})
            arr_news.append(news)
        return arr_news
