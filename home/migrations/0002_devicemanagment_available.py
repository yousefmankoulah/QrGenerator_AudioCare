# Generated by Django 3.2.7 on 2022-11-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicemanagment',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
