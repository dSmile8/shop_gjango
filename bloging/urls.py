from django.urls import path
from bloging.apps import BlogingConfig
from bloging.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogingConfig.name
urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]