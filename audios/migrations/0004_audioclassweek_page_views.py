# Generated by Django 3.1.7 on 2021-03-27 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audios', '0003_auto_20210304_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='audioclassweek',
            name='page_views',
            field=models.IntegerField(default=0),
        ),
    ]