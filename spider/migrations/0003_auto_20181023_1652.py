# Generated by Django 2.1.2 on 2018-10-23 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0002_auto_20181023_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='content',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='time',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
