from django.contrib import admin
from .models import Balance, BalanceEntry, Ticker


class BalanceEntryAdmin(admin.ModelAdmin):
    list_display = ("balance", "create_date")
    date_hierarchy = "create_date"


admin.site.register(Balance)
admin.site.register(Ticker)
admin.site.register(BalanceEntry, BalanceEntryAdmin)
