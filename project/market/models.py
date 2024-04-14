from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name="Category", null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class CoverType(models.Model):
    type = models.CharField(max_length=50, verbose_name="Type")

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Cover"
        verbose_name_plural = "Covers"


class Author(models.Model):
    Full_name = models.CharField(max_length=50, verbose_name="Name")

    def __str__(self):
        return self.Full_name

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"


class Books(models.Model):
    name = models.CharField(verbose_name="Title", max_length=255)
    page_count = models.IntegerField(verbose_name="Page Count")
    category = models.CharField(max_length=200, verbose_name="Category", null=True)
    author = models.ForeignKey(Author, verbose_name="Author", on_delete=models.CASCADE)
    cover = models.ForeignKey(CoverType, verbose_name="Cover", null=True, on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name="Price", max_digits=6, decimal_places=2)
    image = models.ImageField(verbose_name="Image")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
