from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MonitoringSerializer, VirtualsSerializer
from .models import Monitoring, Virtuals
from django.shortcuts import get_object_or_404
import json

class MonitoringListView(APIView):
    def get(self, request):
        monitorings = Monitoring.objects.all()
        serializer = MonitoringSerializer(monitorings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MonitoringSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MonitoringDetailView(APIView):
    def get(self, request, monitoring_id):
        monitoring = get_object_or_404(Monitoring, pk=monitoring_id)
        serializer = MonitoringSerializer(monitoring)
        return Response(serializer.data)

    def delete(self, request, monitoring_id):
        monitoring = get_object_or_404(Monitoring, pk=monitoring_id)
        monitoring.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class VirtualsListView(APIView):
    def get(self, request):
        virtuals = Virtuals.objects.all()
        serializer = VirtualsSerializer(virtuals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VirtualsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VirtualsDetailView(APIView):
    def get(self, request, vm_id):
        virtual_machine = get_object_or_404(Virtuals, pk=vm_id)
        serializer = VirtualsSerializer(virtual_machine)
        return Response(serializer.data)

    def delete(self, request, vm_id):
        virtual_machine = get_object_or_404(Virtuals, pk=vm_id)
        virtual_machine.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
