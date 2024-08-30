from django.contrib import admin
from .models import Orders
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ["address", "kg", "price", "debt", "give", ]
    ordering=["date", "debt"]
    search_fields=["address"]
    list_display_links=["address", "kg",]
    list_editable=["give", ]
    list_per_page=10