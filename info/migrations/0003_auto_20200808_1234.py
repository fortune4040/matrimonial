# Generated by Django 3.0.2 on 2020-08-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20200808_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
