from rest_framework import views
from rest_framework.response import Response

from .models import BTCPrice
from .btc_utils import fetch_prices


class BTCRateAPIView(views.APIView):

    def get(self, request):
        btc = BTCPrice.objects.all().order_by('-fetch_date').first()
        if not btc:
            return Response({'error': 'No data recoded locally'})

        rates = {
            "open": btc.open_price,
            "high": btc.high_price,
            "low": btc.low_price,
            "close": btc.close_price,
            "volume": btc.volume,
            "date": btc.fetch_date,
        }
        return Response({"message": "btc rate", "rates": rates})

    def post(self, request):
        prices = fetch_prices()
        if len(prices) == 0:
            return Response({"error": "error fetching data"})

        sorted_prices = sorted(prices, key=lambda x: x.fetch_date)
        btc = sorted_prices[-1]
        rates = {
            "open": btc.open_price,
            "high": btc.high_price,
            "low": btc.low_price,
            "close": btc.close_price,
            "volume": btc.volume,
            "date": btc.fetch_date,
        }
        return Response({"message": "btc rate", "rates": rates})
