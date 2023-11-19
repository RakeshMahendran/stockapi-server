from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (
    AxisBankStockData, HindalcoStockData, InfosysStockData,
    LTStockData, SBILifeStockData, TCSStockData
)
from .serializers import (
    AxisBankStockDataSerializer, HindalcoStockDataSerializer,
    InfosysStockDataSerializer, LTStockDataSerializer,
    SBILifeStockDataSerializer, TCSStockDataSerializer
)


class AxisBankStockDataViewSet(viewsets.ModelViewSet):
    queryset = AxisBankStockData.objects.all()
    serializer_class = AxisBankStockDataSerializer

class HindalcoStockDataViewSet(viewsets.ModelViewSet):
    queryset = HindalcoStockData.objects.all()
    serializer_class = HindalcoStockDataSerializer

class InfosysStockDataViewSet(viewsets.ModelViewSet):
    queryset = InfosysStockData.objects.all()
    serializer_class = InfosysStockDataSerializer

class LTStockDataViewSet(viewsets.ModelViewSet):
    queryset = LTStockData.objects.all()
    serializer_class = LTStockDataSerializer

class SBILifeStockDataViewSet(viewsets.ModelViewSet):
    queryset = SBILifeStockData.objects.all()
    serializer_class = SBILifeStockDataSerializer

class TCSStockDataViewSet(viewsets.ModelViewSet):
    queryset = TCSStockData.objects.all()
    serializer_class = TCSStockDataSerializer

class AllStockDataAPIView(APIView):
    queryset = AxisBankStockData.objects.none()
    def get(self, request, format=None):
        # Retrieve data from all tables
        axis_bank_data = AxisBankStockData.objects.all()
        hindalco_data = HindalcoStockData.objects.all()
        infosys_data = InfosysStockData.objects.all()
        lt_data = LTStockData.objects.all()
        sbi_life_data = SBILifeStockData.objects.all()
        tcs_data = TCSStockData.objects.all()

        # Serialize data for each table
        axis_bank_serializer = AxisBankStockDataSerializer(axis_bank_data, many=True).data
        hindalco_serializer = HindalcoStockDataSerializer(hindalco_data, many=True).data
        infosys_serializer = InfosysStockDataSerializer(infosys_data, many=True).data
        lt_serializer = LTStockDataSerializer(lt_data, many=True).data
        sbi_life_serializer = SBILifeStockDataSerializer(sbi_life_data, many=True).data
        tcs_serializer = TCSStockDataSerializer(tcs_data, many=True).data

        # Create a dictionary with table names as keys and serialized data as values
        response_data = {
            'axis_bank': axis_bank_serializer,
            'hindalco': hindalco_serializer,
            'infosys': infosys_serializer,
            'lt': lt_serializer,
            'sbi_life': sbi_life_serializer,
            'tcs': tcs_serializer,
        }

        return Response(response_data)
