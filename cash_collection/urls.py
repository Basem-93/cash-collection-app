from django.urls import path
from .views import task_list, next_task, collector_status, collect_cash_from_customer, pay_cash_to_manager, create_task, create_collector

urlpatterns = [
    path('tasks/', task_list, name='task-list'),
    path('next_task/', next_task, name='next-task'),
    path('collector_status/', collector_status, name='collector-status'),
    path('collect/', collect_cash_from_customer, name='collect-cash-from-customer'),
    path('pay/', pay_cash_to_manager, name='pay-cash-to-manager'),
    path('create_task/', create_task, name='create-task'),
    path('create_collector/', create_collector, name='create-collector'),
]
