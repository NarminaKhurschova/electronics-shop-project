"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import *


@pytest.fixture
def product():
    return Item('Телефон', 200, 6)


def test_calculate_total_price(product):
    assert product.calculate_total_price() == 1200


def test_apply_discount(product):
    assert product.apply_discount() == 200.0


def test_all_(product):
    assert product.all != []
