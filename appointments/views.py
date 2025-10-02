from django.shortcuts import render, redirect
from django.conf import settings
from .forms import AppointmentForm
import stripe

# initialize Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def create_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()

            # Build domain (e.g. http://localhost:8000)
            domain_url = request.build_absolute_uri('/')[:-1]

            # Create Stripe checkout session
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[{
                    "price_data": {
                        "currency": "usd",
                        "product_data": {
                            "name": f"Appointment with {appointment.provider_name}",
                        },
                        "unit_amount": appointment.price_cents,
                    },
                    "quantity": 1,
                }],
                mode="payment",
                success_url=domain_url + "/success/?session_id={CHECKOUT_SESSION_ID}",
                cancel_url=domain_url + "/cancel/",
                metadata={"appointment_id": str(appointment.id)},
            )

            # Redirect to Stripe
            return redirect(checkout_session.url, code=303)
    else:
        form = AppointmentForm()

    return render(request, "appointments/create_appointment.html", {"form": form})


def success(request):
    return render(request, "appointments/success.html")


def cancel(request):
    return render(request, "appointments/cancel.html")