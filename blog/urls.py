from django.urls import path
from .views import BlogHomePage

app_name = 'blog'
urlpatterns = [
    path('', BlogHomePage.as_view(), name='blog_home_page'),
]