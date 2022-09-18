import stripe

from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from stripe_test.settings import STRIPE_API_SECRET_KEY
from .models import Item, Order


@api_view(['GET'])
def get_item_stripe_session(request, pk):
    item = get_object_or_404(Item, pk=pk)

    stripe.api_key = STRIPE_API_SECRET_KEY

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'unit_amount_decimal': item.price * 100,
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'https://project-stripe-test.herokuapp.com{reverse("success")}',
        cancel_url=f'https://project-stripe-test.herokuapp.com{reverse("cancel")}',
    )

    return Response({'session_id': session.id})


@api_view(['GET'])
def get_item_buy_form(request, pk):
    item = get_object_or_404(Item, pk=pk)

    context = {
        'item': item,
    }

    response_html = render_to_string(template_name='items/buy_form.html', context=context)

    return Response(response_html)


@api_view(['GET'])
def get_order_stripe_session(request, pk):
    order = get_object_or_404(Order, pk=pk)

    stripe.api_key = STRIPE_API_SECRET_KEY

    if order.discount:
        stripe.Coupon.create(
            id=order.discount.pk,
            percent_off=order.discount.percent_off,
            duration='once'
        )

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': order.currency,
                'unit_amount_decimal': order.sum_price * 100,
                'product_data': {
                    'name': f'Заказ № {order.pk}',
                },
            },
            'quantity': 1,
        }],
        discounts=[{
            'coupon': order.discount.pk,
        }],
        mode='payment',
        success_url=f'https://project-stripe-test.herokuapp.com{reverse("success")}',
        cancel_url=f'https://project-stripe-test.herokuapp.com{reverse("cancel")}',
    )

    return Response({'session_id': session.id})


@api_view(['GET'])
def get_order_buy_form(request, pk):
    order = get_object_or_404(Order, pk=pk)

    context = {
        'order': order,
    }

    response_html = render_to_string(template_name='items/order_buy_form.html', context=context)

    return Response(response_html)


def get_success_form(request):
    return render(request=request, template_name='items/success.html')


def get_cancel_form(request):
    return render(request=request, template_name='items/cancel.html')
