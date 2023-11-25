# Generated by Django 4.2.7 on 2023-11-24 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stories_Vote_Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_img', models.ImageField(upload_to='media/stories/default')),
            ],
        ),
        migrations.CreateModel(
            name='Storis_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/stories/default')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Какое блюдо вам больше нравится?', max_length=150)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storis.option')),
            ],
        ),
        migrations.CreateModel(
            name='Storis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storis.storis_img')),
            ],
        ),
        migrations.CreateModel(
            name='Stories_Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storis.stories_vote_img')),
            ],
        ),
    ]
