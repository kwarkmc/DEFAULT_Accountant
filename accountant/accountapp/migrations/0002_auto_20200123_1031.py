# Generated by Django 3.0.2 on 2020-01-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountant',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='accountant',
            name='pub_date',
            field=models.DateTimeField(default=0),
        ),
        migrations.AddField(
            model_name='accountant',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
