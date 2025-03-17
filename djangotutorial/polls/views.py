
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Monitoring, Virtuals

@method_decorator(csrf_exempt, name='dispatch')
class MonitoringListView(View):
    def get(self, request):
        monitorings = Monitoring.objects.all().values()
        return JsonResponse(list(monitorings), safe=False)
    
    def post(self, request):
        data = json.loads(request.body)
        virtual_machine = get_object_or_404(Virtuals, pk=data.get("virtual_machine"))
        monitoring = Monitoring.objects.create(
            cpu_usage=data["cpu_usage"],
            memory_usage=data["memory_usage"],
            network_traffic=data["network_traffic"],
            monitoring_time=data["monitoring_time"],
            virtual_machines=virtual_machine
        )
        return JsonResponse({"monitoring_id": monitoring.monitoring_id}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class MonitoringDetailView(View):
    def get(self, request, monitoring_id):
        monitoring = get_object_or_404(Monitoring, pk=monitoring_id)
        return JsonResponse({
            "monitoring_id": monitoring.monitoring_id,
            "cpu_usage": monitoring.cpu_usage,
            "memory_usage": monitoring.memory_usage,
            "network_traffic": str(monitoring.network_traffic),
            "monitoring_time": monitoring.monitoring_time.isoformat(),
            "virtual_machine": str(monitoring.virtual_machines.id)
        })
    
    def delete(self, request, monitoring_id):
        monitoring = get_object_or_404(Monitoring, pk=monitoring_id)
        monitoring.delete()
        return JsonResponse({"message": "Deleted successfully"}, status=204)

@method_decorator(csrf_exempt, name='dispatch')
class VirtualsListView(View):
    def get(self, request):
        virtuals = Virtuals.objects.all().values()
        return JsonResponse(list(virtuals), safe=False)
    
    def post(self, request):
        data = json.loads(request.body)
        virtual_machine = Virtuals.objects.create(
            hostname=data["hostname"],
            protocol=data["protocol"],
            user_id_id=data["user_id"],
            address=data["address"],
            port=data["port"],
            user_vm=data["user_vm"],
            password_vm=data["password_vm"],
            ignore_cert=data["ignore_cert"]
        )
        return JsonResponse({"id": virtual_machine.id}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class VirtualsDetailView(View):
    def get(self, request, vm_id):
        virtual_machine = get_object_or_404(Virtuals, pk=vm_id)
        return JsonResponse({
            "id": virtual_machine.id,
            "hostname": virtual_machine.hostname,
            "protocol": virtual_machine.protocol,
            "user_id": virtual_machine.user_id.id,
            "address": virtual_machine.address,
            "port": virtual_machine.port,
            "user_vm": virtual_machine.user_vm,
            "password_vm": virtual_machine.password_vm,
            "ignore_cert": virtual_machine.ignore_cert
        })
    
    def delete(self, request, vm_id):
        virtual_machine = get_object_or_404(Virtuals, pk=vm_id)
        virtual_machine.delete()
        return JsonResponse({"message": "Deleted successfully"}, status=204)
