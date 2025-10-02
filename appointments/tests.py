### ✅ Example Unit Tests (`appointments/tests.py`)

import pytest
from django.urls import reverse
from django.test import Client
from appointments.models import Appointment
from unittest.mock import patch

@pytest.mark.django_db
def test_create_appointment_model():
    appt = Appointment.objects.create(
        provider_name="Dr. Smith",
        appointment_time="2025-10-10 10:00:00",
        client_email="test@example.com"
    )
    assert appt.provider_name == "Dr. Smith"
    assert Appointment.objects.count() == 1

@pytest.mark.django_db
def test_create_appointment_view(client):
    url = reverse("create_appointment")
    resp = client.get(url)
    assert resp.status_code == 200
    assert b"Book an Appointment" in resp.content

@pytest.mark.django_db
@patch("appointments.views.stripe.PaymentIntent.create")
def test_stripe_payment_flow(mock_payment, client):
    mock_payment.return_value = {"id": "pi_test123"}

    data = {
        "provider_name": "Dr. Jane",
        "appointment_time": "2025-11-01 15:00:00",
        "client_email": "user@example.com",
    }
    url = reverse("create_appointment")
    resp = client.post(url, data)
    assert resp.status_code == 302  # redirect to Stripe Checkout or success
    mock_payment.assert_called_once()