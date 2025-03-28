from django.contrib import admin
from django.urls import path, include

from payments.views import ClickWebhookAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("payment/click/update/", ClickWebhookAPIView.as_view()),
    path("", include("payments.urls")),
]
