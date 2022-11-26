from api.services import BaseService
from api_news.models import News


class NewsService(BaseService):
    @classmethod
    def create_list_news(cls, arr_news, topic):
        objs = (
            News(
                title=news.get("title"),
                post_at=news.get("post_at"),
                thumbnail=news.get("thumbnail"),
                topic=topic,
                source=news.get("source"),
                author=news.get("author"),
                excerpt=news.get("excerpt"),
            )
            for news in arr_news
        )
        return objs
