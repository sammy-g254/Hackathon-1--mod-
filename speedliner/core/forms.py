from django import forms
from .models import Customer, Booking, Vehicle, Payment

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'contact_info', 'location']

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['name', 'number_plate', 'capacity', 'available']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'vehicle', 'service_date', 'return_date']
        widgets = {
            'service_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'return_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['vehicle'].queryset = Vehicle.objects.filter(available=True) | Vehicle.objects.filter(pk=self.instance.vehicle.pk)
        else:
            self.fields['vehicle'].queryset = Vehicle.objects.filter(available=True)


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['booking', 'amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Exclude bookings that already have a payment
        self.fields['booking'].queryset = Booking.objects.exclude(payments__isnull=False)
