# Generated by Django 2.1.4 on 2021-11-01 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('InstagramApp', '0019_auto_20211101_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='total',
        ),
    ]