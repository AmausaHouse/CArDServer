# Generated by Django 2.1.7 on 2019-02-21 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_nn_index',
            field=models.IntegerField(null=True),
        ),
    ]
