from operator import imod
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    headline = models.CharField(max_length=200, default="Headline")
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index')