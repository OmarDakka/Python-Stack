from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("/post_message", views.create_post),
    path("/post_comment/<int:post_id>", views.create_comment),
    # path("/delete_message", views.delete_post)
]
