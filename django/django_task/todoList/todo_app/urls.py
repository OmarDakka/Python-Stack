from django.urls import path
from . import views


#URLs here are simple, following the RESTful method with only adding an id to each the category url or the task url in order to do a specific
#function on a specific category and task, otherwise the category url or the task url will create a new category or task following
#the function.
urlpatterns = [
    path('', views.index),
    path('category', views.category_api.as_view()),
    path('category/<int:id>', views.category_api.as_view()),
    path('task', views.task_api.as_view()),
    path('task/<int:id>', views.task_api.as_view())
]
