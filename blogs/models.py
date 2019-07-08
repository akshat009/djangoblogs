from django.db import models


class BlogPost(models.Model):

    title = models.TextField()
    content = models.TextField(null=True,blank=True)
    image_url = models.CharField(max_length=208, null=True)
    slug = models.SlugField(unique=True)




