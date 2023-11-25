# Generated by Django 4.2.7 on 2023-11-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='name',
        ),
        migrations.AlterField(
            model_name='application',
            name='delivery_time',
            field=models.CharField(choices=[('1', '12:00'), ('2', '12:30')], max_length=2),
        ),
    ]
