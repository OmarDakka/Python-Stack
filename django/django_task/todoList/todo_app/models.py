import json
from json.encoder import JSONEncoder
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from login_app.models import users

## A class in order to do validations but doesnt currently work.
class UserManager(models.Model):
    def form_validator(self, post_data):
        errors = {}
        if len(post_data['categoryTitle']) == 0:
            errors["categoryTitle"] = "Category title is required!"
        return errors

## Category Model that includes all the details needed for a category with a function in order to return the data in JSON form
class Category(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        users, related_name="categories_created", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def to_json(self):
        tasks = Task.objects.filter(category = self)

        task_result = []

        for task in tasks:
            task_result.append(task.to_json())
        
        return {
            "id": self.id,
            "title" : self.title,
            "tasks": task_result
        }

## Task Model that includes all the details needed for a task with a function in order to return the data in JSON form
class Task(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        users, related_name="tasks_created", on_delete=CASCADE)
    category = models.ForeignKey(
        Category, related_name="task_category", on_delete=CASCADE)
    description = models.TextField()
    duedate = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            "id": self.id,
            "title" : self.title,
            "description": self.description,
            "duedate": self.duedate
        }