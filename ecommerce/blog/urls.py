from django.urls import path
from blog.views import create_article


urlpatterns = [
    path('article/', create_article, name="article"),
]
