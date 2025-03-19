from rest_framework import serializers
from .models import Monitoring, Virtuals

class MonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoring
        fields = ['monitoring_id', 'cpu_usage', 'memory_usage', 'network_traffic', 'monitoring_time', 'virtual_machines']

class VirtualsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Virtuals
        fields = ['id', 'hostname', 'protocol', 'user_id', 'address', 'port', 'user_vm', 'password_vm', 'ignore_cert']
