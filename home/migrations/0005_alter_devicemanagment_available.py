# Generated by Django 3.2.7 on 2022-11-14 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_devicemanagment_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicemanagment',
            name='available',
            field=models.BooleanField(default=False),
        ),
    ]