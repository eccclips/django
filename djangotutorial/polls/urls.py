from django.urls import path
from .views import MonitoringListView, MonitoringDetailView, VirtualsListView, VirtualsDetailView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('monitoring/', MonitoringListView.as_view(), name='monitoring-list'),
    path('monitoring/<int:monitoring_id>/', MonitoringDetailView.as_view(), name='monitoring-detail'),
    path('virtuals/', VirtualsListView.as_view(), name='virtuals-list'),
    path('virtuals/<uuid:vm_id>/', VirtualsDetailView.as_view(), name='virtuals-detail'),
]

