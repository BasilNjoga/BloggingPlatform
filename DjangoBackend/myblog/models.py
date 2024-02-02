from django.db import models
from django.contrib.postgres import fields as postgresFields



class UserBlog(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    body = models.TextField(default="")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)


    def __str__(self):
        return self.title + " - " + self.created_by
