from api.services import BaseService
from api_news.models import News, Image


class ImageService(BaseService):
    @classmethod
    def create_list_image(cls, data, news_objs):
        image_data = []
        for _idx, news in enumerate(data):
            images = news.get("images")
            for img in images:
                item = {
                    "news": news_objs[_idx],
                    "title": img["title"],
                    "src": img["src"],
                }
                image_data.append(item)
        image_objs = (Image(**img) for img in image_data)
        return image_objs
