# Generated by Django 2.1 on 2018-08-26 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='remember_token',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
