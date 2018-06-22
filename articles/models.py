from django.db import models
from django.urls import reverse


class Category(models.Model):

    name = models.CharField('категория', max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


class Article(models.Model):
    name = models.CharField('название', max_length=50)
    summary = models.TextField('краткое описание', max_length=100)
    description = models.TextField('статья')
    image = models.ImageField('фотография', upload_to='articles/images', default='', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'category': self.category.slug, 'slug': self.slug})


