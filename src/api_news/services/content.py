from api.services import BaseService
from api_news.models import News, Content


class ContentService(BaseService):
    @classmethod
    def create_list_content(cls, data, news_objs):
        content_data = []
        for _idx, news in enumerate(data):
            contents = news.get("content")
            for content in contents:
                item = {
                    "news": news_objs[_idx],
                    "paragraph": content.get("paragraph"),
                    "order": content.get("order"),
                }
                content_data.append(item)
        content_objs = (Content(**content) for content in content_data)
        return content_objs
