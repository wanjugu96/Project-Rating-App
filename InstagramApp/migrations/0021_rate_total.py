# Generated by Django 2.1.4 on 2021-11-01 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InstagramApp', '0020_remove_rate_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='total',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]