import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from order.factories import UserFactory, OrderFactory
from product.factories import ProductFactory
from order.models import Order


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        self.product = ProductFactory(title="pro controller", price=200.00)

    def test_create_order(self):
        data = json.dumps({
            "user": self.user.id,
            "products_id": [self.product.id],
        })

        response = self.client.post(
            reverse("order-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        order_data = json.loads(response.content)

        # aqui sim: order.product é lista de produtos
        self.assertEqual(order_data["product"][0]["title"], self.product.title)
        self.assertEqual(order_data["product"][0]["price"], self.product.price)