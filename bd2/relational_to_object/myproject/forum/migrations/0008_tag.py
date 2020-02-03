# Generated by Django 3.0.2 on 2020-02-02 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20200202_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Topic')),
            ],
        ),
    ]
