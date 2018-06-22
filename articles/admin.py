from django.contrib import admin
from .models import Article, Category


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ['name', 'summary', 'category']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']

