from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Sum, DecimalField
from django.db.models.functions import Coalesce

from .constants import CURRENCIES


class Order(models.Model):
    currency = models.CharField(
        max_length=3,
        choices=CURRENCIES,
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    @property
    def sum_price(self):
        return self.items.aggregate(
            total_price=Coalesce(
                Sum('price'),
                0,
                output_field=DecimalField()
            )
        ).get('total_price')


class Item(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=(MinValueValidator(Decimal('0.01')),),
    )
    currency = models.CharField(
        max_length=3,
        choices=CURRENCIES,
    )
    order = models.ForeignKey(
        to='Order',
        on_delete=models.PROTECT,
        related_name='items',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Discount(models.Model):
    percent_off = models.IntegerField(
        validators=(
            MinValueValidator(1),
            MaxValueValidator(100),
        ),
    )
    order = models.OneToOneField(
        to='Order',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='discount',
    )

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f'{self.percent_off}%'
