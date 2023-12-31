# Generated by Django 4.2.7 on 2023-11-24 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=6)),
                ('desc', models.TextField()),
                ('calorie', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('carbohydrate', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('type', models.IntegerField()),
            ],
            options={
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overall_rating', models.IntegerField(blank=True, null=True)),
                ('speed_grade', models.BooleanField(blank=True, null=True)),
                ('taste_grade', models.BooleanField(blank=True, null=True)),
                ('comment', models.TextField()),
            ],
        ),
    ]
