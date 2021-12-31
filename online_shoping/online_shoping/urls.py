from account import views as v
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home),
    path('product-',include(('product.urls','product'),namespace="product")),
    path('account-',include(('account.urls','account'),namespace="account")),
    path('order-',include(('orderapp.urls','orderapp'),namespace="orderapp")),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
