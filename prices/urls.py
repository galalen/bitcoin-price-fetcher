from django.urls import path

from .views import BTCRateAPIView

urlpatterns = [
    path('quotes', BTCRateAPIView.as_view(), name='quotes'),
]
