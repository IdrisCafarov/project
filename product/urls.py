from django.urls import path
from product.views import index_view,view_api,product_detail,delete_product,detail_api

app_name = "product"
urlpatterns = [
    path('',index_view,name="index"),
    path('api_view',view_api,name="view_api"),
    path('api_view/<id>/',detail_api,name="detail_api"),
    path('product_detail/<slug>/',product_detail,name="product_detail"),
    path('product_delete/<id>/',delete_product,name="delete_product"),
]
