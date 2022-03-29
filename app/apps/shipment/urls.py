from django.urls import path

from .views import ShipmentCreateView, ShipmentUpdateView, ShipmentListView, ShipmentDeleteView, ShipmentSentView

app_name = 'shipment'

urlpatterns = [
    path('create/', ShipmentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ShipmentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ShipmentDeleteView.as_view(), name='delete'),
    path('list/', ShipmentListView.as_view(), name='list'),
    path('sent/<int:pk>/', ShipmentSentView.as_view(), name='sent'),
]