from django.db import models
from django.urls import reverse
from django.contrib import auth
from django.utils import timezone
# SuperUserInformation
# User: Jose
# Email: training@pieriandata.com
# Password: testpassword

class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def get_absolute_url(self):
        return reverse("myblog:post_details",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('myblog.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("myblog:post_list")

    def __str__(self):
        return self.text
