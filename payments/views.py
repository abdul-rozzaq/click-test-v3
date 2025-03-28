from django.shortcuts import render
from click_up.views import ClickWebhook

from .utils import generate_pay_link

class ClickWebhookAPIView(ClickWebhook):
    def successfully_payment(self, params):
        """
        successfully payment method process you can ovveride it
        """
        print(f"payment successful params: {params}")

    def cancelled_payment(self, params):
        """
        cancelled payment method process you can ovveride it
        """
        print(f"payment cancelled params: {params}")


def home_page(request):
    context = {}

    return render(request, "index.html", context)
