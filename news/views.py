from django.shortcuts import render
from django.views.generic import ListView
from .models import Article, Category


class HomeView(ListView):
    model = Article
    template_name = 'news/home.html'
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        return Article.objects.filter(is_published=True).select_related('category', 'author', 'author__user')


class CategoryView(ListView):
    model = Article
    template_name = 'news/category.html'
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        return Article.objects.filter(is_published=True, category=self.category).select_related('author', 'author__user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context