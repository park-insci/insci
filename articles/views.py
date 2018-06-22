from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse


class ArticleListView(ListView):
    model = Article
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleListView, self).get_context_data(*args, **kwargs)
        context['articles'] = self.model.objects.all()
        return context


class CategoryListView(ListView):

    model = Category
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView, self).get_context_data(*args, **kwargs)
        context['categories'] = self.model.objects.all()
        return context


class CategoryDetailView(DetailView):

    model = Category
    template_name = 'articles/category_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['categories'] = self.model.objects.all()
        context['category'] = self.get_object()
        context['articles_from_category'] = self.get_object().article_set.all()
        return context


class ArticleDetailView(DetailView):

    model = Article
    template_name = 'articles/article_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['categories'] = self.model.objects.all()
        context['article'] = self.get_object()

        return context
