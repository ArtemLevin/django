from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404

from app_1.models import User, Order


def user_orders(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user).order_by('-pk')
    orders_7 = Order.objects.filter(customer=user).filter(order_date__gte=datetime.now() - timedelta(days=7)).order_by(
        '-pk')
    orders_30 = Order.objects.filter(customer=user).filter(
        order_date__gte=datetime.now() - timedelta(days=30)).order_by('-pk')
    orders_365 = Order.objects.filter(customer=user).filter(
        order_date__gte=datetime.now() - timedelta(days=365)).order_by('-pk')
    return render(request, 'app_1/user_orders.html', {'user': user, 'orders': orders,
                                                      'orders_7': set(orders_7),
                                                      'orders_30': set(orders_30) - set(orders_7),
                                                      'orders_365': set(orders_365) - set(orders_30) - set(orders_7)})
