# Generated by Django 4.2.6 on 2023-11-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_user_email_verification_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_verification_token',
            field=models.UUIDField(null=True),
        ),
    ]
