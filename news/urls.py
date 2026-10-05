from django.urls import path
from .views import HomeView, CategoryView

app_name = 'news'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categoria/<slug:slug>/', CategoryView.as_view(), name='category'),
]