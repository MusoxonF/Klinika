# Generated by Django 5.0.3 on 2024-03-17 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tashxis',
            old_name='sick',
            new_name='diagnoz',
        ),
        migrations.AddField(
            model_name='tashxis',
            name='tashxis',
            field=models.TextField(blank=True, null=True),
        ),
    ]
