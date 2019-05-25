from django.db import models
from features.models import Features
from django.utils.timezone import localtime


class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=10, blank=True)
    town_or_city = models.CharField(max_length=50, blank=False)
    street_address1 = models.CharField(max_length=50, blank=False)
    street_address2 = models.CharField(max_length=50, blank=False)
    county = models.CharField(max_length=50, blank=False)
    date = models.DateField(default=localtime, blank=False, editable=False)
    total_price = models.IntegerField(blank=False)

    def __str__(self):
        return "{0}. {1} - {2}".format(self.id, self.date.strftime('%d.%m.%Y %H:%M'), self.full_name)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    feature = models.ForeignKey(Features, null=False)
    qty = models.IntegerField(blank=False)
    price = models.IntegerField(blank=False, editable=False)

    def __str__(self):
        return "{0} - {1} &euro;{2}".format(self.qty, self.order.date.strftime('%d.%m.%Y %H:%M'),
                                            self.price)
