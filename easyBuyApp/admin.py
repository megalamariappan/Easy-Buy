from django.contrib import admin
from .models import categories,offer,products,card,payment,orders

# Register your models here.
admin.site.register(categories)
admin.site.register(offer)
admin.site.register(products)
admin.site.register(card)
admin.site.register(payment)
admin.site.register(orders)