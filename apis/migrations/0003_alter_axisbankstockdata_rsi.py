# Generated by Django 4.2.7 on 2023-11-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_alter_axisbankstockdata_deliverable_percent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='axisbankstockdata',
            name='RSI',
            field=models.DecimalField(blank=True, decimal_places=20, max_digits=30, null=True),
        ),
    ]
