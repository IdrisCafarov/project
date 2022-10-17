from ctypes import addressof
from itertools import product
from django.shortcuts import render,get_object_or_404,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import MainCategory,SubCategory,Product,AdsSettings
from product.serializers import ProductSerializer
from django.http import HttpResponse
from django.template.defaulttags import register

# Create your views here.


def index_view(request):
    main_categories = MainCategory.objects.all()
    ads = AdsSettings.objects.all()
    sub_categories = SubCategory.objects.all()
    products = Product.objects.all()

    context = {
        "main_categories":main_categories,
        "ads":ads,
        "sub_categories":sub_categories,
        "products":products
    }
    for x in products:
        print(x.get_absolute_url)
    
    return render(request,'homepage/homepage-3.html',context)

def product_detail(request,slug):
    context = {}
    product = get_object_or_404(Product,slug=slug)
    context['product'] = product


    return render(request,"product_detail/product_detail.html",context)

def delete_product(request,id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect(request.META['HTTP_REFERER'])
    



@api_view(['GET'])
def view_api(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detail_api(request,id):
    products = Product.objects.filter(id=id)
    serializer = ProductSerializer(products,many=True)
    return Response(serializer.data)


@register.filter
def exclude_product(self,product):
    result = self.exclude(id=product.id)
    return result