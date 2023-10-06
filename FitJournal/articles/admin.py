from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.contrib.gis import forms

from articles.models import BaseArticle, Article, Categories

admin.site.register(Categories)


class ArticleAdminForm(forms.ModelForm):
    """
    Форма в которой указываем для какого поля и какой модели будет использован CKEditor
    """
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


@admin.register(BaseArticle)
class BaseArticleAdmin(admin.ModelAdmin):
    # Предзаполнение полей
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Article)
class ArticleAdmin(BaseArticleAdmin):
    form = ArticleAdminForm

