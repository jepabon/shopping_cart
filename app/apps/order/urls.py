from django.urls import path

from .views import OrderCreateView, OrderUpdateView, OrderListView, OrderDeleteView

app_name = 'order'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='delete'),
    path('list/', OrderListView.as_view(), name='list'),
]