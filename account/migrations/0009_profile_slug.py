# Generated by Django 2.0.1 on 2018-01-09 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20180102_0224'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='user_example', unique=True),
            preserve_default=False,
        ),
    ]