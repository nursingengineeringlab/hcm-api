# Generated by Django 3.1.7 on 2021-02-25 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_api', '0004_auto_20210213_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='senior',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
