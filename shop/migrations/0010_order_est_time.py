# Generated by Django 3.0.7 on 2020-06-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200625_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='est_time',
            field=models.DateTimeField(null=True),
        ),
    ]
