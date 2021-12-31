from django.shortcuts import render,redirect
from .models import Category,Product
def get_by_category(request,id):
    cl=Category.objects.all()
    pl=Product.objects.filter(category=id)
    d={'cl':cl,'pl':pl}
    return render(request,'home.html',d)


def search_product(request):
    cl=Category.objects.all()
    if request.method=='POST':
        srch=request.POST.get('srch')
        pl=Product.objects.filter(name__contains=srch)
        d={'cl':cl,'pl':pl}
        return render(request,'search.html',d)
    else:
        pl=Product.objects.all()
        d={'cl':cl,'pl':pl}
        return render(request,'search.html',d)