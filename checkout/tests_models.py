from django.test import TestCase
from .models import Order, OrderItem
import datetime


class TestModels(TestCase):

    @staticmethod
    def create_order():
        return Order(
            full_name='Test test',
            phone_number='088 888 88 88',
            country='Ireland',
            postcode='RD1111',
            town_or_city='Dublin',
            street_address1='Example street',
            street_address2='Example street',
            county='Dublin',
            total_price=50
        )

    def test_order_model_name(self):
        order = self.create_order()

        self.assertEqual(Order.__str__(order), '{0}. {1} - Test test'
                         .format(order.id, datetime.datetime.now().strftime('%d.%m.%Y %H:%M')))

    def test_order_item_model_name(self):
        order = self.create_order()
        order_item = OrderItem(
            order=order,
            qty=1,
            price=50
        )
        self.assertEqual(OrderItem.__str__(order_item), '{0} - {1} &euro;{2}'.
                         format(order_item.qty, datetime.datetime.now().strftime('%d.%m.%Y %H:%M'),
                                order_item.price))
