# Generated by Django 3.2.9 on 2021-11-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='pid',
            field=models.CharField(max_length=10, verbose_name='Номер аптеки'),
        ),
    ]
