from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from users.forms import *


# Create your views here.

def buyer_view(request,id):
    context = {}

    usr = get_object_or_404(User, id=id)

    if request.method == 'POST' and 'btn_buyer'in request.POST:
        form = BuyerDetailForm(request.POST, request.FILES or None, instance=usr)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sizin postunuz uğurla yeniləndi!')
            return HttpResponseRedirect('/buyer/')
    else:
        form_b = BuyerDetailForm(instance=usr)

    

    if request.method == 'POST' and 'btn_buyer'in request.POST:
        form = BuyerDetailForm(request.POST, request.FILES or None, instance=usr)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sizin postunuz uğurla yeniləndi!')
            return HttpResponseRedirect('/buyer/')
    else:
        form_s = SellerDetailForm(instance=usr)


    context['form_s'] = form_s

    

    return render(request,"user_buyer/user_information/user_information.html",context)


def buyer_notification(request,id):
    usr = get_object_or_404(User, id=id)

    return render(request,"user_buyer/notifications/notifications.html")

def buyer_invoice(request,id):
    usr = get_object_or_404(User, id=id)

    return render(request,"user_buyer/invoice/invoices.html")

def buyer_wishlist(request,id):
    usr = get_object_or_404(User, id=id)

    return render(request,"user_buyer/wishlist/whishlist.html")


def buyer_adress(request,id):
    usr = get_object_or_404(User, id=id)

    return render(request,"user_buyer/adress/addresses.html")



def seller_dashboard(request,id):
    usr = get_object_or_404(User, id=id)

    return render(request,"user_seller/free_seller.html")

def seller_view(request,id):
    context = {}

    usr = get_object_or_404(User, id=id)

    if request.method == 'POST':
        form = SellerDetailForm(request.POST, request.FILES or None, instance=usr)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sizin postunuz uğurla yeniləndi!')
            return HttpResponseRedirect('/buyer/')
        else:
            context['form'] = form

    context['form'] = SellerDetailForm(instance=usr)


    return render(request,"user_buyer/user_information/user_buyer.html",context)
