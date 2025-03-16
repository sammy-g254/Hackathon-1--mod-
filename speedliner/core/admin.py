

# Register your models here.
from django.contrib import admin
from .models import Customer, Booking, Vehicle, Payment

admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Vehicle)
admin.site.register(Payment)
