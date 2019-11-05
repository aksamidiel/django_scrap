from django.db import models


class Category(models.Model):
    root_category = models.ForeignKey("self", blank=True, null=True)
    name = models.CharField(max_length=255)
    urls = models.TextField(blank=True)
    sort = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["sort"]
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    category = models.ForeignKey("Category")
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    image = models.ImageField(blank=True, upload_to="product/")
    description = models.TextField(blank=True)
    sort = models.IntegerField(default=0)
    urls = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["sort"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
