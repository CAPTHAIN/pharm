# Generated by Django 3.2.9 on 2021-11-16 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='city',
        ),
        migrations.AlterField(
            model_name='medicine',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категорія'),
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(db_index=True, max_length=200, verbose_name='Адреса')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.city', verbose_name='Місто')),
            ],
            options={
                'verbose_name': 'Точка',
                'verbose_name_plural': 'Точки',
            },
        ),
        migrations.AddField(
            model_name='medicine',
            name='point',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.point', verbose_name='Точка'),
        ),
    ]
