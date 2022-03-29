from django.urls import path

from .views import ProductCreateView, ProductUpdateView, ProductListView, ProductDeleteView

app_name = 'product'

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('list/', ProductListView.as_view(), name='list'),
]