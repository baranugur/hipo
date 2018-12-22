from django.shortcuts import render
from django.core.paginator import Paginator
from .flickr import Flickr


def index(request):
    tag = request.GET.get('tag')
    flickr = Flickr(tag)
    params = {}
    response = flickr.search(params)
    image_list = flickr.get_images(response)

    paginator = Paginator(image_list, 6)
    page = request.GET.get('page')
    images = paginator.get_page(page)
    return render(request, 'photo/index.html', {'images': images, 'tag': tag})
