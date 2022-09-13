from django.urls import path
from users.views import buyer_view, buyer_notification, buyer_invoice, buyer_adress, buyer_wishlist,seller_dashboard

app_name="user"

urlpatterns = [
    path('user_info/<id>/',buyer_view,name="buyer_info"),
    path('buyer_notifications/<id>/',buyer_notification,name="buyer_notf"),
    path('buyer_invoice/<id>/',buyer_invoice,name="buyer_invoice"),
    path('buyer_adress/<id>/',buyer_adress,name="buyer_adress"),
    path('buyer_wishlist/<id>/',buyer_wishlist,name="buyer_wishlist"),
    path('seller_dashboard/<id>/',seller_dashboard,name ='seller_dashboard')
    ]
