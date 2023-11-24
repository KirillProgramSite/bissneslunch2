# Generated by Django 4.2.7 on 2023-11-23 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0014_remove_menu_review_menu_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviewThrough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asntement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.review')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.menu')),
            ],
            options={
                'verbose_name': 'Связь оценки блюда и блюда',
                'verbose_name_plural': 'Связи оценок блюд и блюд',
            },
        ),
        migrations.AlterField(
            model_name='menu',
            name='Review',
            field=models.ManyToManyField(through='Menu.reviewThrough', to='Menu.review'),
        ),
    ]