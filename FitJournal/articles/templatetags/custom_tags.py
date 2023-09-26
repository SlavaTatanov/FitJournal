from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    """
    Переводит текст отформатированный как MARKDOWN в HTML
    """
    return mark_safe(markdown.markdown(text))
