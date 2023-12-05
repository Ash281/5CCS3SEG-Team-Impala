# Generated by Django 4.2.6 on 2023-12-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_remove_task_assignees_task_assignees'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='hours_spent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
