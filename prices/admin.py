from django.contrib import admin

from .models import BTCPrice


@admin.register(BTCPrice)
class BTCPriceAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'low_price', 'high_price', 'open_price', 'close_price', 'volume')
