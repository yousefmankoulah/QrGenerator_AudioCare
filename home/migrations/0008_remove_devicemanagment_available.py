# Generated by Django 3.2.7 on 2022-11-14 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20221114_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devicemanagment',
            name='available',
        ),
    ]
