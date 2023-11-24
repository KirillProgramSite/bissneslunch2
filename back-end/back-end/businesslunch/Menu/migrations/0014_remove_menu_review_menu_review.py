# Generated by Django 4.2.7 on 2023-11-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0013_remove_menu_review_menu_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='Review',
        ),
        migrations.AddField(
            model_name='menu',
            name='Review',
            field=models.ManyToManyField(blank=True, null=True, to='Menu.review'),
        ),
    ]