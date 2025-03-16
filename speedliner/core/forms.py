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
            # Only show available vehicles
            self.fields['vehicle'].queryset = Vehicle.objects.filter(is_available=True)

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['booking', 'amount']
