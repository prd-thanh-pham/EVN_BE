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
<<<<<<< HEAD
                    "title": content.get("title"),
                    "paragraph": content.get("paragraph"),
                    "description_img": content.get("description_img"),
                    "image": content.get("image"),
=======
                    "paragraph": content.get("title"),
>>>>>>> parent of 0d3b301 (fix bug)
                    "order": content.get("order"),
                }
                content_data.append(item)
        content_objs = (Content(**content) for content in content_data)
        return content_objs
