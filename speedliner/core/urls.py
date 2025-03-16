from django.urls import path
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from .views import (
    CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView,
    BookingListView, BookingDetailView, BookingCreateView, BookingUpdateView, BookingDeleteView,
    VehicleListView, VehicleCreateView, VehicleUpdateView, VehicleDeleteView,
    PaymentListView, PaymentCreateView, PaymentUpdateView, PaymentDeleteView,
)

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),

    # Customer URLs
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/add/', CustomerCreateView.as_view(), name='customer_add'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_edit'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    # Booking URLs
    path('bookings/', BookingListView.as_view(), name='booking_list'),
    path('bookings/add/', BookingCreateView.as_view(), name='booking_add'),
    path('bookings/<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('bookings/<int:pk>/edit/', BookingUpdateView.as_view(), name='booking_edit'),
    path('bookings/<int:pk>/delete/', BookingDeleteView.as_view(), name='booking_delete'),

    # Vehicle URLs
    path('vehicles/', VehicleListView.as_view(), name='vehicle_list'),
    path('vehicles/add/', VehicleCreateView.as_view(), name='vehicle_add'),
    path('vehicles/<int:pk>/edit/', VehicleUpdateView.as_view(), name='vehicle_edit'),
    path('vehicles/<int:pk>/delete/', VehicleDeleteView.as_view(), name='vehicle_delete'),

    # Payment URLs
    path('payments/', PaymentListView.as_view(), name='payment_list'),
    path('payments/add/', PaymentCreateView.as_view(), name='payment_add'),
    path('payments/<int:pk>/edit/', PaymentUpdateView.as_view(), name='payment_edit'),
    path('payments/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment_delete'),
]
