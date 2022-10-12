from api.services import BaseService
from api_news.models import News


class NewsService(BaseService):
    @classmethod
    def create_list_news(cls, arr_news):
        objs = (
            News(
                title=news.get("title"),
                post_at=news.get("post_at"),
                thumbnail=news.get("thumbnail"),
                source=news.get("source"),
                content=news.get("content"),
                author=news.get("author"),
                excerpt=news.get("excerpt")
            )
            for news in arr_news
        )
        return objs
