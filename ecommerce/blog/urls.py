from django.urls import path
from blog.views import List_articles, Detail_article, Create_article, Delete_article


urlpatterns = [
    #path('article/', create_article, name="article"),
    path('list-articles/', List_articles.as_view(), name="list_articles"), #Al usar una class agregamos el .as_view()
    path('detail-article/<int:pk>/', Detail_article.as_view(), name="detail_article"),
    path('create-article/', Create_article.as_view(), name="create_article"),
    path('delete-article/<int:pk>/', Delete_article.as_view(), name="delete_article"),
]
