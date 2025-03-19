import datetime
import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Protocol(models.TextChoices):
    RDP = 'rdp', 'RDP'
    SSH = 'ssh', 'SSH'
    VNC = 'vnc', 'VNC'
    

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


class Virtuals(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
    )
    hostname = models.CharField(max_length=32)
    protocol = models.CharField(
        max_length=5,
        choices=Protocol.choices
    )
    user_id = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=128)
    port = models.IntegerField()
    user_vm = models.CharField(max_length=64)
    password_vm = models.CharField(max_length=128)
    ignore_cert = models.BooleanField()

class Monitoring(models.Model):
    monitoring_id = models.UUIDField(primary_key=True)
    cpu_usage = models.FloatField()
    memory_usage = models.FloatField()
    network_traffic = models.TimeField()
    monitoring_time = models.DateTimeField()
    virtual_machines = models.ForeignKey(Virtuals, on_delete=models.CASCADE)

    def __str__(self):
        return f"Monitoring {self.monitoring_id}: CPU {self.cpu_usage}%, Memory {self.memory_usage}%, Traffic {self.network_traffic}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
      
    def __init__(self):
        #: Doc comment for instance attribute qux.
        self.qux = 3

        self.spam = 4
        """Docstring for instance attribute spam."""