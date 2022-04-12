from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Symbol(models.Model):
    name = models.CharField(max_length=16, unique=True)
    full_name = models.CharField(max_length=64)
    description = models.TextField(max_length=512)
    url = models.CharField(max_length=256)


class Article(models.Model):
    title = models.CharField(max_length=256, unique=True)
    guid = models.CharField(max_length=64)
    description = models.TextField(max_length=512)
    link = models.CharField(max_length=256)
    published = models.DateTimeField()
    slug = models.SlugField(unique=True, max_length=255)
    symbol = models.CharField(max_length=16, unique=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)