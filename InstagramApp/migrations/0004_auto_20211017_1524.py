# Generated by Django 2.1.4 on 2021-10-17 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InstagramApp', '0003_auto_20211017_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]
