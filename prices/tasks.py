from celery import shared_task

from .models import BTCPrice
from .btc_utils import fetch_prices


@shared_task
def log_prices():
    logs = fetch_prices()
    if len(logs) > 0:
        BTCPrice.objects.bulk_create(logs)
        print(f"Logged prices {len(logs)}")
