import pytest

from product.factories import CategoryFactory
from product.serializers.category_serializer import CategorySerializer


@pytest.mark.django_db
def test_category_serializer_fields():
    category = CategoryFactory()
    serializer = CategorySerializer(category)

    data = serializer.data

    assert data["title"] == category.title
    assert data["slug"] == category.slug
    assert data["description"] == category.description
    assert data["active"] == category.active
