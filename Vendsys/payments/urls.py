from django.urls import path
from api.views.payment_api import CreatePaymentAPIview,payment_success,payment_cancle

urlpatterns = [
    path("create/", CreatePaymentAPIview.as_view(), name="create-payment"),
    path("payment-success/", payment_success, name="payment-success"),
    path("payment-cancle/", payment_cancle, name="payment-cancle"),
]