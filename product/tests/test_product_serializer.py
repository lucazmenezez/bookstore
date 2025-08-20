import pytest

from order.factories import OrderFactory
from product.factories import ProductFactory
from order.serializers.order_serializer import OrderSerializer


@pytest.mark.django_db
def test_order_serializer_total_and_products():
    product1 = ProductFactory(price=100)
    product2 = ProductFactory(price=200)
    order = OrderFactory(product=[product1, product2])

    serializer = OrderSerializer(order)
    data = serializer.data

    assert "total" in data
    assert data["total"] == product1.price + product2.price
    assert len(data["product"]) == 2
