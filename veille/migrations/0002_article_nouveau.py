# Generated by Django 3.2.3 on 2021-05-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veille', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='nouveau',
            field=models.BooleanField(default=0, max_length=55),
        ),
    ]