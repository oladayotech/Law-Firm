from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('news/create', views.news_create, name='news_create'),
    path('news/edit/<slug:headline_for_url>', views.news_edit, name='news_edit'),
    path('news/<slug:headline_for_url>', views.news_detail, name='news_detail'),
    path('people', views.people, name='people')
]