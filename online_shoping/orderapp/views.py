from django.shortcuts import render,redirect
from .models import Cart,Product,User,Order
from product.models import Category
def addtocart(request,id):
    uid=request.session.get('uid')
    c=Cart()
    product=Product.objects.get(id=id)
    user=User.objects.get(id=uid)
    c.product=product
    c.user=user
    c.save()
    return redirect('/')

def cart_list(request):
    uid=request.session.get('uid')
    cr=Cart.objects.filter(user=uid)
    cl=Category.objects.all()
    if request.method=='POST':
        odr=Order()
        total=request.POST.get('totalbill')
        odr.totalBill=int(total)
        odr.user=User.objects.get(id=uid)
        odr.save()
        for i in cr:
            i.delete()
        return redirect('/')
    else:
        totalBill=0
        for i in cr:
            totalBill=totalBill+i.product.price
        d={'cr':cr,'cl':cl,'totalbill':totalBill}
        return render(request,'cartlist.html',d)

def my_order(request):
    uid=request.session.get('uid')
    orl=Order.objects.filter(user=uid)
    cl=Category.objects.all()
    d={'cl':cl,'orl':orl}
    return render(request,'my_order.html',d)
