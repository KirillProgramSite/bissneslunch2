# Generated by Django 4.2.7 on 2023-11-23 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0012_alter_review_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='Review',
        ),
        migrations.AddField(
            model_name='menu',
            name='Review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Menu.review'),
        ),
    ]
