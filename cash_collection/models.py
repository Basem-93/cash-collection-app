from django.db import models
from django.utils import timezone


class CashCollector(models.Model):
    """
    Model representing a Cash Collector.
    """
    name = models.CharField(max_length=100)
    is_frozen = models.BooleanField(default=False)
    frozen_since = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def check_freeze_status(self):
        """
        Check if the collector should be frozen based on the collected amount and duration.
        """
        collected_money = 0
        for task in self.tasks.all():
            # only calculate collected money that not yet paid to the manager
            if not task.paid_to_manager:
                collected_money += task.amount_due
                if collected_money >= 5000:
                    if task.collected_at and timezone.now() - task.collected_at >= timezone.timedelta(days=2):
                        self.is_frozen = True
                        self.frozen_since = timezone.now()
                        self.save()
                        break


class Task(models.Model):
    """
    Model representing a Task for cash collection.
    """
    collector = models.ForeignKey(CashCollector, on_delete=models.CASCADE, related_name='tasks')
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=255)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_due_at = models.DateTimeField(default=timezone.now)
    collected_at = models.DateTimeField(null=True, blank=True)
    paid_to_manager = models.BooleanField(default=False)

    def __str__(self):
        return f"Task for {self.customer_name}"
