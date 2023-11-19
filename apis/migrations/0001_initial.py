# Generated by Django 4.2.7 on 2023-11-18 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AxisBankStockData',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Date', models.DateField()),
                ('Open_Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('High_Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Low_Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Close_Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Prev_Close_Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Total_Traded_Quantity', models.IntegerField()),
                ('Total_Traded_Value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Week_High_Price_52', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Week_Low_Price_52', models.DecimalField(decimal_places=2, max_digits=10)),
                ('VWAP', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Deliverable_Volume', models.IntegerField()),
                ('Deliverable_Percent', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('Series', models.CharField(max_length=5)),
                ('RSI', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('Upper_Band', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('Middle_Band', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('Lower_Band', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('Percent_K', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('Percent_D', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('MACD', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('Signal_Line', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('MA', models.DecimalField(blank=True, decimal_places=6, max_digits=10, null=True)),
                ('RSI_Recommendation', models.CharField(max_length=10)),
                ('Bollinger_Recommendation', models.CharField(max_length=10)),
                ('Stochastic_Recommendation', models.CharField(max_length=10)),
                ('MACD_Recommendation', models.CharField(max_length=10)),
                ('MA_Recommendation', models.CharField(max_length=10)),
            ],
        ),
    ]