from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('add_two',views.addTwo),
    path('destroy', views.destroy),
    path('add',views.add)
]