from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.



def cart_details(request):
    return render(request,'cart.html')

def c_id(request):
    ct_id=request.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id

def add_cart(request,product_id):
    prod=products.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.quan < c_items.prodt.stock:
            c_items.quan+=1
            c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quan=1,cart=ct)
        c_items.save()
    return redirect('cartDetails')


def min_cart(request):
    pass

def cart_delete(request):
    pass
