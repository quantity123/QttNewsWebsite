# Generated by Django 3.0.1 on 2020-01-28 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20200128_0323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='userName',
        ),
    ]
