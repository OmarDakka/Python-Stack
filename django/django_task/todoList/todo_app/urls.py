from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('category', views.category_api.as_view()),
    path('category/<int:id>', views.category_api.as_view()),
    path('task', views.task_api.as_view()),
    path('task/<int:id>', views.task_api.as_view())
]
