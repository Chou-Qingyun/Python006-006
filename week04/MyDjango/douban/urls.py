from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('scrapy', views.scrapy),
    path('comments/<int:id>', views.comment, name='comment')
]