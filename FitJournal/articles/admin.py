from django.contrib import admin
from articles.models import BaseArticle, Article, Categories

admin.site.register(Categories)


@admin.register(BaseArticle)
class BaseArticleAdmin(admin.ModelAdmin):
    # Предзаполнение полей
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Article)
class ArticleAdmin(BaseArticleAdmin):
    pass

