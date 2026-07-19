from django.urls import path
from api.views.payment_api import (CreatePaymentAPIview,
                                   payment_success,
                                   payment_cancel,
                                   stripe_webhook)

urlpatterns = [
    path("create/", CreatePaymentAPIview.as_view(), name="create-payment"),
    path("payment-success/", payment_success, name="payment-success"),
    path("payment-cancel/", payment_cancel, name="payment-cancel"),
    path("webhook/", stripe_webhook, name="stripe-webhook"),
]