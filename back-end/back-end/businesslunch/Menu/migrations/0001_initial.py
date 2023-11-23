# Generated by Django 4.2.7 on 2023-11-22 13:40

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
                ('name', models.CharField(max_length=300)),
                ('weight', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('compound', models.TextField(blank=True, null=True)),
                ('calories', models.IntegerField()),
                ('proteins', models.IntegerField()),
                ('carbohydrates', models.IntegerField()),
                ('fats', models.IntegerField()),
                ('type', models.IntegerField()),
                ('review', models.IntegerField(null=True)),
                ('speed', models.IntegerField(null=True)),
                ('comment', models.TextField(null=True)),
            ],
            options={
                'ordering': ['type'],
            },
        ),
    ]
