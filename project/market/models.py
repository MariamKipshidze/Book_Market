from django.db import models

# Create your models here.


class Books(models.Model):
    name = models.CharField(verbose_name="Title", max_length=255)
    page_count = models.IntegerField()
    category = models.CharField(verbose_name="Category", max_length=200)
    author = models.CharField(verbose_name="Author", max_length=200)
    price = models.DecimalField(verbose_name="Price", max_digits=6, decimal_places=2)
    image = models.ImageField()
