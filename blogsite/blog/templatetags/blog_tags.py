from django import template
from ..models import Post
from ..models import Recipe  # Import the Recipe model
from django.db.models import Count
import markdown
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def total_posts():
 return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts} 


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]


# Recipe Tags
@register.simple_tag
def total_recipes():
    """Returns the total number of published recipes"""
    return Recipe.objects.filter(status=Recipe.Status.PUBLISHED).count()

@register.inclusion_tag('recipes/latest_recipes.html')
def show_latest_recipes(count=5):
    latest_recipes = Recipe.published.order_by('-publish')[:count]
    return {'latest_recipes': latest_recipes}

@register.simple_tag
def get_most_commented_recipes(count=5):
    """Returns the most commented recipes"""
    return Recipe.objects.filter(status=Recipe.Status.PUBLISHED).annotate(
        total_responses=Count('responses')
    ).order_by('-total_responses')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))