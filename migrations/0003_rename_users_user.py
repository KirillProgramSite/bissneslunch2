# Generated by Django 4.2.7 on 2023-11-23 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('user', '0002_rename_user_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='User',
        ),
    ]