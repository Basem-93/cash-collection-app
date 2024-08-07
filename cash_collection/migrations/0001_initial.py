# Generated by Django 5.0.6 on 2024-07-03 06:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CashCollector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_frozen', models.BooleanField(default=False)),
                ('frozen_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_address', models.TextField()),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount_due_at', models.DateTimeField()),
                ('collected_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('collected_at', models.DateTimeField(blank=True, null=True)),
                ('cash_collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='cash_collection.cashcollector')),
            ],
        ),
    ]
