# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=255)
    pubdate = models.DateTimeField('publish date')
    category = models.ManyToManyField('Category')

    def __str__(self):
        return self.title

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category
