# Generated by Django 3.0.8 on 2020-08-02 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_manager', '0003_auto_20200802_2131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='lesson',
            new_name='lessons',
        ),
    ]
