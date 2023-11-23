# Generated by Django 4.2.7 on 2023-11-23 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Menu', '0008_alter_basket_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
