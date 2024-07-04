from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CashCollector, Task
from .serializers import TaskSerializer, CashCollectorSerializer


@api_view(['GET'])
def task_list(request):
    """
    Retrieve list of tasks.
    """
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def next_task(request):
    """
    Retrieve the next task for a specific collector.
    """
    collector_id = request.data.get('collector_id')
    task = Task.objects.filter(collector_id=collector_id, collected_at__isnull=True).first()

    if not task:
        return Response({"detail": "No tasks available."}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['GET'])
def collector_status(request):
    """
    Get the status of a cash collector.
    """
    collector_id = request.data.get('collector_id')
    collector = get_object_or_404(CashCollector, pk=collector_id)
    collector.check_freeze_status()  # Check and update freeze status
    serializer = CashCollectorSerializer(collector)
    return Response(serializer.data)


@api_view(['POST'])
def collect_cash_from_customer(request):
    """
    Update the collected cash for a task.
    """
    task_id = request.data.get('task_id')
    task = get_object_or_404(Task, pk=task_id)
    # Check and update the freeze status of the collector
    task.collector.check_freeze_status()
    if task.collector.is_frozen:
        return Response('this collector is frozen, please go to the manager to pay latest collected cash')
    task.collected_at = timezone.now()
    task.save()

    # Check and update the freeze status of the collector
    task.collector.check_freeze_status()

    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['POST'])
def pay_cash_to_manager(request):
    """
    Handle cash delivery to the manager.
    """
    collector_id = request.data.get('collector_id')
    collector = get_object_or_404(CashCollector, pk=collector_id)

    # Mark collector as unfrozen and reset the frozen_since timestamp
    collector.is_frozen = False
    collector.frozen_since = None
    collector.save()

    # Update all collected tasks to mark them as paid to the manager
    tasks = Task.objects.filter(collector=collector, collected_at__isnull=False)
    tasks.update(paid_to_manager=True)

    serializer = CashCollectorSerializer(collector)
    return Response(serializer.data)


@api_view(['POST'])
def create_task(request):
    """
    Create a new task for cash collection.
    """
    data = request.data
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_collector(request):
    """
    Create a new cash collector.
    """
    data = request.data
    serializer = CashCollectorSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)