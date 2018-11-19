from django.contrib.auth.models import AbstractUser
from markdownx.utils import markdownify

# class CustomUser(AbstractUser):
#     email = models.CharField(max_length=200)

from django.db import models

from django.utils import timezone

# if using djangos default user model
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from django.template.defaultfilters import slugify
from django.urls import reverse
import markdown2


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    body = models.TextField()
    body2 = MarkdownxField(default='')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    @property
    def to_markdown(self):
        return markdown2.markdown(self.body2)

    def get_absolute_url(self):
        return reverse('page', kwargs={'slug': self.slug})


class Post(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField(default='', editable=False)
    body = models.TextField()
    body2 = MarkdownxField(default='')

    date_posted = models.DateTimeField(default=timezone.now)
    # slug = models.SlugField()
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts',
                               default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
    #

    @property
    def to_markdown(self):
        # return markdown2.markdown(self.body2)
        return markdownify(self.body2)



    def __str__(self):
        return self.title

