# Generated by Django 3.0.1 on 2020-01-28 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20200118_2107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['pk'], 'verbose_name': '分类', 'verbose_name_plural': '分类'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['pk'], 'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
    ]