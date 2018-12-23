from django.db import models
from django.conf import settings
from django.utils import timezone


class PreviousSearch(models.Model):
    searched_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=200)
    searched_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.keyword

    def insert(self, searched_by, keyword, searched_date):
        self.searched_by = searched_by
        self.keyword = keyword
        self.searched_date = searched_date
        self.save()
