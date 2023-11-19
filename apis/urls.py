# yourapp/urls.py
from django.urls import path
from .views import AxisBankStockDataViewSet, HindalcoStockDataViewSet, InfosysStockDataViewSet,LTStockDataViewSet, SBILifeStockDataViewSet, TCSStockDataViewSet, AllStockDataAPIView



app_name = 'apis'

urlpatterns = [
    path('api/axisbankstockdata/', AxisBankStockDataViewSet.as_view({'get': 'list'}), name='axisbankstockdata-list'),
    path('api/hindalcostockdata/', HindalcoStockDataViewSet.as_view({'get': 'list'}), name='hindalcostockdata-list'),
    path('api/infosysstockdata/', InfosysStockDataViewSet.as_view({'get': 'list'}), name='infosysstockdata-list'),
    path('api/ltstockdata/', LTStockDataViewSet.as_view({'get': 'list'}), name='ltstockdata-list'),
    path('api/sbilifestockdata/', SBILifeStockDataViewSet.as_view({'get': 'list'}), name='sbilifestockdata-list'),
    path('api/tcsstockdata/', TCSStockDataViewSet.as_view({'get': 'list'}), name='tcsstockdata-list'),



    path('api/aggregated_stock_data/', AllStockDataAPIView.as_view(), name='all_stock_data'),
]
