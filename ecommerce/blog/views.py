from re import template
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from blog.models import Articles

# Create your views here.

""" def create_article(request):
    new_article = Articles.objects.create(
        title = "Bajó el bitcoin",
        description = "Esperar a comprar",
        author = "Alejandro Díaz Alvarado"
    )

    context = {
        'new_article': new_article
    }

    return render(request, 'article.html', context=context) """

class List_articles(ListView):
    model = Articles
    template_name = 'list_articles.html'

class Detail_article(DetailView):
    model = Articles
    template_name = 'detail_article.html'

class Create_article(CreateView):
    model = Articles
    template_name = 'create_article.html'
    success_url = '/blog/list-articles'
    fields = '__all__'

class Delete_article(DeleteView):
    model = Articles
    template_name = 'delete_article.html'
    success_url = '/blog/list-articles'

""" class Update_article(UpdateView):
    model = Articles
    success_url = '/blog/list-articles' """
