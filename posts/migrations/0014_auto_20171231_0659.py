# Generated by Django 2.0 on 2017-12-31 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_posts_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=60, null=True),
        ),
    ]