from blog.models import Post
from django import template

register = template.Library()

@register.simple_tag
def get_posts():
    posts = Post.objects.all()
    return posts
