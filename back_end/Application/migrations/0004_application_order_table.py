# Generated by Django 4.2.7 on 2023-11-24 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Application', '0003_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='order_table',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Application.table'),
        ),
    ]