from typing import Text
from django.db import models
from datetime import date,datetime
from login.models import users


class posts(models.Model):
    text = models.TextField()
    owners = models.ForeignKey(users, related_name="ownerz", on_delete = models.CASCADE,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class comments(models.Model):
    comment = models.TextField()
    owner = models.ForeignKey(users,related_name = "owners", on_delete = models.CASCADE)
    post = models.ForeignKey(posts,related_name="message", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def post_creation(text, users):
    created_post = posts.objects.create(text = text, owners = users)
    return created_post

def comment_creation(comment,owner,post_id):
    created_comment = comments.objects.create(comment = comment, owner = owner, post = posts.objects.get(id = post_id))
    return created_comment

# def post_deletion(post_id):
#     remove = posts.objects.get(id = post_id)
#     remove.delete()
#     return remove
    