from django.urls import path
from.import views
urlpatterns = [
    path('admin_order',views.admin_order,name='admin_order'),
    path('admin_cancel_order/<int:order_id>/',views.admin_cancel_order,name='admin_cancel_order'),
    path('add_address',views.add_address,name='add_address'),

    path('user_order/',views.user_order,name='user_order'),
    path('place_order/',views.place_order,name='place_order'),
    path('order_place/',views.order_place,name='order_place'),


    path('order_details/<int:order_id>/',views.order_details,name='order_details'),
    path('cancel_order/<int:order_id>/',views.cancel_order,name='cancel_order'),
    path('return_update/<int:order_id>/',views.return_update,name='return_update'),
    path('admin_order_update/<int:order_id>/',views.admin_order_update,name='admin_order_update'),

    path('checkout/',views.checkout,name='checkout'),
    path('ordrsuccess',views.ordrsuccess,name='ordrsuccess'),

    path('proceed-to-pay/',views.razorpaycheck,name='razorpaycheck'),
    path('my_orders',views.my_orders,name='my_orders'),

    path('return_order/<int:order_id>/',views.return_order,name='return_order')

]