# Generated by Django 3.2 on 2023-01-27 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20230127_0247'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='rank',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]