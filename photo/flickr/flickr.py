from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
import json
from .image import Image

API_KEY = "1ddb7df62cbdc4e07f6ec75ca78e2960"

class Flickr:
    def __init__(self):        
        self.url_base = "https://api.flickr.com/services/rest/"
        self.url_api = self.url_base
        self.api_key = API_KEY
        self.format = "json"
        self.nojsoncallback = "1"

    def search(self, params):
        missing_params = {
            "method": "flickr.photos.search", 
            "api_key": self.api_key,
            "format": self.format,
            "nojsoncallback": self.nojsoncallback,
        }
        params.update(missing_params)
        return requests.get(self.url_api, params=params)


    def get_images(self, response):
        json_data = json.loads(response.text)
        photos_dictionary = json_data.get("photos")
        images = []
        if photos_dictionary:
            photos = photos_dictionary.get("photo")
            for photo in photos:
                image_url = self.build_image_url_string(photo)
                image_title = photo.get("title")
                image = Image(image_title, image_url)
                images.append(image)
        return images
    
    def paginate_images(self, page, images):
        paginator = Paginator(images, 16)
        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            images = paginator.page(1)
        except EmptyPage:
            images = paginator.page(paginator.num_pages)
        return images

    def build_image_url_string(self, photo):
        # https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
        image_url = ("https://farm" + str(photo["farm"]) + ".staticflickr.com/" +
                        str(photo["server"]) + "/" + str(photo["id"]) + "_" +
                        str(photo["secret"]) + ".jpg")
        return image_url
