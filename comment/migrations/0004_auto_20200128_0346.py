# Generated by Django 3.0.1 on 2020-01-28 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20200128_0329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='userName',
            new_name='user',
        ),
    ]