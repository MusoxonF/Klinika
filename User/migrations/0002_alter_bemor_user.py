# Generated by Django 5.0.3 on 2024-03-17 09:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bemor',
            name='user',
            field=models.ForeignKey(default='uchirilgan_user', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='bemor_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
