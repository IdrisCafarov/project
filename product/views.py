from ctypes import addressof
from django.shortcuts import render
from product.models import MainCategory,SubCategory,Product,AdsSettings

# Create your views here.


def index_view(request):
    main_categories = MainCategory.objects.all()
    ads = AdsSettings.objects.all()
    sub_categories = SubCategory.objects.all()

    context = {
        "main_categories":main_categories,
        "ads":ads,
        "sub_categories":sub_categories
    }
    
    return render(request,'homepage/homepage.html',context)