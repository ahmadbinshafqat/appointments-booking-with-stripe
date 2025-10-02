from django.db import models

class Appointment(models.Model):
    provider_name = models.CharField(max_length=200)
    appointment_time = models.DateTimeField()
    client_email = models.EmailField()
    price_cents = models.IntegerField(default=5000)  # $50 default

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.provider_name} - {self.client_email} at {self.appointment_time}"