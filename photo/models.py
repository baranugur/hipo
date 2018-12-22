from django.db import models

class PreviousSearch(models.Model):
    keyword = models.CharField(max_length=200)