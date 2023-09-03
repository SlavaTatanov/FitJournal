from django.shortcuts import render
from django.http import HttpRequest
from articles.models import BaseArticle, Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def articles_list(request: HttpRequest):
    """
    Представление обрабатывает список статей
    """
    # Извлекаем все статьи
    all_articles = Article.published.all()
    # Указываем какие объекты разбивать на странице и по сколько
    paginator = Paginator(all_articles, 5)
    # Берем параметры с гет запроса, если их нет дефолтное 1
    page_number = request.GET.get('page', 1)
    try:
        articles_page = paginator.page(page_number)
    except EmptyPage or PageNotAnInteger:
        articles_page = paginator.page(1)
    context = {'title': 'Статьи', 'articles': articles_page}
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


def article(req: HttpRequest, article_slug):
    """
    Представление обычной статьи.
    Получаем первую статью с данным slug.
    Добавляем title/
    """
    article_obj = Article.published.filter(slug=article_slug).first()
    context = {'article': article_obj,
               'title': article_obj.title}
    return render(req, 'articles/article.html', context=context)

