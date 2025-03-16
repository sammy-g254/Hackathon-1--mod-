from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    contact_info = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    name = models.CharField(max_length=200)
    number_plate = models.CharField(max_length=20, unique=True)  # New field for vehicle number plate
    capacity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    
    def __str__(self):
        # This string will be used in the Booking form's drop-down
        return f"{self.name} ({self.number_plate})"

class Booking(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="bookings")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="bookings")
    service_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Mark vehicle as unavailable when booking is created
        if self.vehicle.available:
            self.vehicle.available = False
            self.vehicle.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Restore vehicle availability when booking is deleted
        self.vehicle.available = True
        self.vehicle.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Booking for {self.customer.name} on {self.service_date}"

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Payment of {self.amount} for {self.booking}"
