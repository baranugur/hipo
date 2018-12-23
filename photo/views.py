from django.shortcuts import render
from django.core.paginator import Paginator
from django.utils import timezone
from .flickr import Flickr
from .models import PreviousSearch


def index(request):
    tag = request.GET.get('tag')
    page = request.GET.get('page')

    flickr = Flickr(tag)
    params = {}
    response = flickr.search(params)
    image_list = flickr.get_images(response)
    paginator = Paginator(image_list, 6)
    
    if tag and not page:
        search = PreviousSearch()
        search.insert(request.user, tag.lower(), timezone.now())

    images = paginator.get_page(page)
    previous_searches = PreviousSearch.objects.filter(searched_date__lte=timezone.now()).order_by('-searched_date').distinct()[:20]
    return render(request, 'photo/index.html', {'images': images, 'previous_searches': previous_searches})
