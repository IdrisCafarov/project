from django.urls import path
from product.views import index_view

app_name = "product"
urlpatterns = [
    path('',index_view,name="index")
]
