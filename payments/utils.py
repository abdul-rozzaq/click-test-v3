import time
import hashlib
import requests

from django.conf import settings
from click_up import ClickUp


CLICK_API_URL = "https://api.click.uz/v2/merchant/payment/ofd_data/submit_items"


click_up = ClickUp(service_id=settings.CLICK_SERVICE_ID, merchant_id=settings.CLICK_MERCHANT_ID)


def generate_pay_link(user_id, amount) -> str:
    return click_up.initializer.generate_pay_link(id=user_id, amount=amount, return_url="https://example.com")


print(generate_pay_link("7984654", 1000))


def generate_auth_header():
    timestamp = str(int(time.time()))
    digest = hashlib.sha1(f"{timestamp}{settings.CLICK_SECRET_KEY}".encode()).hexdigest()
    auth_header = f"{settings.CLICK_MERCHANT_USER_ID}:{digest}:{timestamp}"
    return auth_header


def create_invoice(amount, phone_number, merchant_trans_id):
    url = f"https://api.click.uz/v2/merchant/invoice/create"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Auth": generate_auth_header(),
    }
    data = {"service_id": settings.CLICK_SERVICE_ID, "amount": amount, "phone_number": phone_number, "merchant_trans_id": merchant_trans_id}
    response = requests.post(url, json=data, headers=headers)
    return response.json()
