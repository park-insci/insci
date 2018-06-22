from django.conf.urls import url

from articles.views import ArticleListView, CategoryListView, CategoryDetailView, ArticleDetailView

urlpatterns = [

    url(r'^$', ArticleListView.as_view(), name='base_articles'),
    url(r'^$', CategoryListView.as_view(), name='base_categories'),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^(?P<category>[-\w]+)/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail'),
]
