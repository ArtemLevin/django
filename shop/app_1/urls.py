from django.urls import path

from .views import user_orders

urlpatterns = [
    path('user_orders/<int:user_id>/', user_orders, name='user_orders'),

]
