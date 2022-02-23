import requests
from django.utils import timezone
from django.conf import settings
from celery import shared_task

from .models import BTCPrice


def fetch_prices():
    market_code = 'USD'
    date = str(timezone.now().date())

    response = requests.get(f"https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol=BTC&market={market_code}&interval=60min&apikey={settings.ALPHA_API_KEY}")
    if response.status_code != 200:
        return []

    data = response.json()
    prices = data['Time Series Crypto (60min)']
    hours_range = range(1, 25)
    logs = []
    for i in hours_range:
        timestamp = "{} {:02d}:00:00".format(date, i)
        if timestamp not in prices:
            continue

        record = prices[timestamp]
        logs.append(
            BTCPrice(
                market_code=market_code,
                fetch_date=timestamp,
                open_price=record.get('1. open', 0),
                high_price=record.get('2. high', 0),
                low_price=record.get('3. low', 0),
                close_price=record.get('4. close', 0),
                volume=record.get('5. volume', 0),
            )
        )

    return logs


@shared_task
def log_prices():
    logs = fetch_prices()
    if len(logs) > 0:
        BTCPrice.objects.bulk_create(logs)
        print(f"Logged prices {len(logs)}")
