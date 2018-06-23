from django.conf.urls import url

from articles.views import ArticleListView, CategoryListView, CategoryDetailView, ArticleDetailView
from articles.views import article_list

urlpatterns = [

    url(r'^$', article_list,  name='home'),
    #url(r'^$', CategoryListView.as_view(), name='base_categories'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
]
