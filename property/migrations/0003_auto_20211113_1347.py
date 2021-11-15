# Generated by Django 3.2.8 on 2021-11-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20211025_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='age_in_years',
            field=models.CharField(blank=True, default='', max_length=2, null=True, verbose_name='Age (In Years)'),
        ),
        migrations.AlterField(
            model_name='property',
            name='zipcode',
            field=models.CharField(default='', max_length=9, verbose_name='Zip Code'),
        ),
    ]