# Generated by Django 2.1.2 on 2018-10-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=300)),
            ],
        ),
    ]