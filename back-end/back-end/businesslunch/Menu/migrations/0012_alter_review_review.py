# Generated by Django 4.2.7 on 2023-11-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0011_alter_review_review_delete_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.IntegerField(blank=True, choices=[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')], default=0, null=True),
        ),
    ]