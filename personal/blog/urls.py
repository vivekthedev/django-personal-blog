from django.urls import path
from .views import home, post, blog_list, about, contact, search, search_tag
app_name = 'blog'


urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog_list, name='blog_list'),
    path('post/<id>/<slug:post>', post, name='post'),
    path('about-me', about, name='about-me'),
    path('contact-me', contact, name='contact-me'),
    path('results',  search, name='search'),
    path('results/tag/<slug:tag_slug>',  search_tag, name='search-tag'),
]
