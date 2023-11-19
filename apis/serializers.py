# yourapp/serializers.py
from rest_framework import serializers
from .models import AxisBankStockData, HindalcoStockData, InfosysStockData, LTStockData, SBILifeStockData, TCSStockData, AggregatedStockData

class AxisBankStockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AxisBankStockData
        fields = '__all__'

class HindalcoStockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HindalcoStockData
        fields = '__all__'

class InfosysStockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfosysStockData
        fields = '__all__'

class LTStockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = LTStockData
        fields = '__all__'

class SBILifeStockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SBILifeStockData
        fields = '__all__'

class TCSStockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TCSStockData
        fields = '__all__'


class AggregatedStockDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AggregatedStockData
        fields = '__all__'

