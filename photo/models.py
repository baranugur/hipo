from django.db import models
from django.conf import settings
from django.utils import timezone


class PreviousSearch(models.Model):
    keyword = models.CharField(max_length=200)
    searched_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.keyword

    def initialize(self, keyword, searched_date):
        self.keyword = keyword
        self.searched_date = searched_date
