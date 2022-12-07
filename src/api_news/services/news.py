from api.services import BaseService
from api_news.models import News


class NewsService(BaseService):
    @classmethod
    def create_list_news(cls, arr_news, topic):
        in_db_sources = topic.news.values_list("source", flat=True)
        source_crawl = list(
            filter(lambda x: x.get("source") not in in_db_sources, arr_news)
        )
        if source_crawl:
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
                for news in source_crawl
            )
            return source_crawl, objs
        return source_crawl, []
