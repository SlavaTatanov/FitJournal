from django.shortcuts import render
from articles.models import BaseArticle


def about(request):
    body_text = BaseArticle.objects.filter(slug='about')
    context = {
        'title': "О нас",
        'body_text': body_text[0].body
    }
    return render(request, 'articles/base_article.html', context=context)
