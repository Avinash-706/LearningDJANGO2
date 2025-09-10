from django.db import models
from django.utils import timezone
# Create your models here.


class BookInfo(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    price = models.IntegerField()
    publication_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



