from django.shortcuts import render
from django.utils import timezone
from .flickr.flickr import Flickr
from .models import PreviousSearch


def index(request):
    tag = request.GET.get('tag')
    page = request.GET.get('page')

    flickr = Flickr()
    params = {'tags': tag}
    response = flickr.search(params)
    image_list = flickr.get_images(response)

    if tag and not page:
        tag = tag.strip().lower()
        existing_searches = PreviousSearch.objects.filter(keyword=tag)
        if existing_searches:
            existing_search = existing_searches[0]
            existing_search.searched_date = timezone.now()
            existing_search.save()
        else:
            search = PreviousSearch()
            search.initialize(tag, timezone.now())
            search.save()
    
    images = flickr.paginate_images(page, image_list)
    previous_searches = PreviousSearch.objects.filter(searched_date__lte=timezone.now()).order_by('-searched_date')[:20]
    return render(request, 'photo/index.html', {'images': images, 'previous_searches': previous_searches})
