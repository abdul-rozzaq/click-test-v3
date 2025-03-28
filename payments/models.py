from django.db import models


class Order(models.Model):
    amount = models.FloatField()
    status = models.CharField(max_length=256)

    def __str__(self):
        return super().__str__()


# class Invoice(models.Model):
#     service_id = models.IntegerField()
#     payment_id = models.BigIntegerField(unique=True)
#     name = models.CharField(max_length=255)
#     barcode = models.CharField(max_length=13, blank=True, null=True)
#     spic = models.CharField(max_length=17)
#     package_code = models.CharField(max_length=20)
#     unit_price = models.PositiveIntegerField()  # Mahsulot birligi narxi (tiyinda)
#     amount = models.PositiveIntegerField()  # Miqdor
#     vat = models.PositiveIntegerField()  # QQS (tiyin)
#     vat_percent = models.PositiveIntegerField(default=10)  # QQS foizi
#     received_card = models.PositiveIntegerField()  # Karta orqali to‘langan summa (tiyin)
#     qr_code_url = models.URLField(blank=True, null=True)  # Fiskal chekka havola

#     def total_price(self):
#         return self.unit_price * self.amount

#     def __str__(self):
#         return f"Invoice {self.payment_id} - {self.name}"
