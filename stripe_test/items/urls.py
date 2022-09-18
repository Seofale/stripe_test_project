from django.urls import path

from . import views

urlpatterns = [
    path('buy/<int:pk>/', views.get_item_stripe_session, name='get_item_stripe_session'),
    path('item/<int:pk>/', views.get_item_buy_form, name='get_item_buy_form'),
    path('order/buy/<int:pk>/', views.get_order_stripe_session, name='get_order_stripe_session'),
    path('order/<int:pk>/', views.get_order_buy_form, name='get_order_buy_form'),
    path('success/', views.get_success_form, name='success'),
    path('cancel/', views.get_cancel_form, name='cancel'),
]
