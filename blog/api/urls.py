from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
		path('', views.index),
		path('articles/', views.article_list),
		path('articles/<int:pk>', views.article_details),
		]
