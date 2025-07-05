from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('news/', views.news, name='news'),
    path('news/search', views.news_search, name='news_search'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='careers'),
    path('practices/', views.practices, name='practices'),
    path('practices/<slug:practice_name_for_url>', views.practices_info, name='practices_info'),
    path('news/create', views.news_create, name='news_create'),
    path('news/edit/<slug:headline_for_url>', views.news_edit, name='news_edit'),
    path('news/<slug:headline_for_url>', views.news_detail, name='news_detail'),
    path('people', views.people, name='people'),
    path('people/search', views.people_search, name='people_search'),
    path('people/<slug:name_for_url>', views.people_info, name='people')
]