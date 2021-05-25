from datetime import date, datetime
from django.db import models


# Create your models here.
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['description']) < 10 and len(postData['description']) > 0:
            errors["description"] = "Show description should be at least 10 characters"
        date_time_obj = datetime. strptime(postData['date'], '%Y-%m-%d').date()
        if date_time_obj >= date.today():
            errors["date"] = "Date must be in the past"  
        return errors



class shows(models.Model):
    title = models.CharField(max_length=255, unique=True)
    network = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()