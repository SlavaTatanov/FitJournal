from django.contrib import admin
from articles.models import BaseArticle, Article

admin.site.register(BaseArticle)
admin.site.register(Article)

