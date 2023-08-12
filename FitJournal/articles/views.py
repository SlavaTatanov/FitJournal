from django.shortcuts import render
from django.http import HttpRequest
from articles.models import BaseArticle


def articles_list(request: HttpRequest):
    context = {'title': 'Статьи'}
    return render(request, 'articles/articles.html', context=context)


def about(request: HttpRequest):
    """
    Представление статьи "О нас"
    """
    body_text = BaseArticle.objects.filter(slug='about')
    context = {
        'title': "О нас",
        'body_text': body_text[0].body
    }
    return render(request, 'articles/base_article.html', context=context)
