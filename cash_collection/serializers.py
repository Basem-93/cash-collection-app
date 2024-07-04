from rest_framework import serializers
from .models import CashCollector, Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class CashCollectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashCollector
        fields = '__all__'
