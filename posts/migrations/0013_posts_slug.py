# Generated by Django 2.0 on 2017-12-30 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20171229_0408'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(default='sadasd asdas d', unique=True),
            preserve_default=False,
        ),
    ]
