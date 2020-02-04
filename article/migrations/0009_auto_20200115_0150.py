# Generated by Django 3.0.1 on 2020-01-15 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20200109_2301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='supportCount',
        ),
        migrations.AddField(
            model_name='article',
            name='bodyIconograph',
            field=models.ImageField(blank=True, upload_to='article/%Y%m%d/'),
        ),
        migrations.AddField(
            model_name='article',
            name='isRecommend',
            field=models.BooleanField(default=False),
        ),
    ]
