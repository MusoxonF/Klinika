# Generated by Django 5.0.3 on 2024-03-17 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_bemor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bemor',
            name='user',
        ),
    ]
