from django.urls import path
from .views import MonitoringListView, MonitoringDetailView, VirtualsListView, VirtualsDetailView

urlpatterns = [
    path('monitorings/', MonitoringListView.as_view(), name='monitoring-list'),
    path('monitorings/<int:monitoring_id>/', MonitoringDetailView.as_view(), name='monitoring-detail'),
    path('virtuals/', VirtualsListView.as_view(), name='virtuals-list'),
    path('virtuals/<int:vm_id>/', VirtualsDetailView.as_view(), name='virtuals-detail'),
]
