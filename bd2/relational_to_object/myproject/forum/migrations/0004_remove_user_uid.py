# Generated by Django 3.0.2 on 2020-01-30 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20200130_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='uid',
        ),
    ]
