# Generated by Django 4.1.2 on 2022-11-14 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='emp_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='password',
            new_name='work',
        ),
    ]
