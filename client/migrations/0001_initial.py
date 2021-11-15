# Generated by Django 3.2.8 on 2021-10-25 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(default='', max_length=30, verbose_name='Resident Name')),
                ('mobile_phone', models.CharField(default='0000000000', max_length=10, verbose_name='Mobile Phone Number')),
                ('work_phone', models.CharField(blank=True, default='0000000000', max_length=10, verbose_name='Work Phone Number')),
                ('comments', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
    ]