# Generated by Django 4.2.7 on 2023-11-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0010_grade_alter_menu_review_alter_review_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.IntegerField(blank=True, choices=[(1, 'Очень плохо'), (2, 'Плохо'), (3, 'Нормально'), (4, 'Хорошо'), (5, 'Отлично')], default=0, null=True),
        ),
        migrations.DeleteModel(
            name='Grade',
        ),
    ]