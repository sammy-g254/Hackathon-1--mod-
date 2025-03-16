from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Customer, Booking, Vehicle, Payment
from .forms import CustomerForm, BookingForm, VehicleForm, PaymentForm

# CUSTOMER VIEWS
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')


# BOOKING VIEWS

class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'

class BookingDetailView(DetailView):
    model = Booking
    template_name = 'booking_detail.html'

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingUpdateView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'
    success_url = reverse_lazy('booking_list')

class BookingDeleteView(DeleteView):
    model = Booking
    template_name = 'booking_confirm_delete.html'
    success_url = reverse_lazy('booking_list')



# VEHICLE VIEWS
class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicle_list.html'

class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle_form.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleUpdateView(UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'vehicle_form.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle_list')


# PAYMENT VIEWS
class PaymentListView(ListView):
    model = Payment
    template_name = 'payment_list.html'

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentUpdateView(UpdateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payment_form.html'
    success_url = reverse_lazy('payment_list')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payment_confirm_delete.html'
    success_url = reverse_lazy('payment_list')
