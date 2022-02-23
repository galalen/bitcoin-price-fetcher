from django.db import models


class BTCPrice(models.Model):

    low_price = models.DecimalField(max_digits=10, decimal_places=5)
    high_price = models.DecimalField(max_digits=10, decimal_places=5)
    open_price = models.DecimalField(max_digits=10, decimal_places=5)
    close_price = models.DecimalField(max_digits=10, decimal_places=5)
    volume = models.IntegerField()
    market_code = models.CharField(max_length=100)
    fetch_date = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "btc_prices"
        ordering = ["-fetch_date"]
