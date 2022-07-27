from django.shortcuts import render
from blog.models import Articles

# Create your views here.

def create_article(request):
    new_article = Articles.objects.create(
        title = "Bajó el bitcoin",
        description = "Esperar a comprar",
        author = "Alejandro Díaz Alvarado"
    )

    context = {
        'new_article': new_article
    }

    return render(request, 'article.html', context=context)