"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path
from django.conf.urls import  url

from django.conf import settings
from django.conf.urls.static import static,settings

from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

# from products.views import \
#     (ProductListView,\
#     product_list_view,\
#     ProductDetailView,\
#     product_detail_view,\
#     ProductFeaturedDetailView,\
#     ProductFeaturedListView,\
#     ProductDetailSlugView)

from product.views import ProductListView,ProductDetailView,ProductFeaturedDetailView,ProductFeaturedListView,ProductDetailSlugView



from pproducts.views import product_upload,product_list_view,product_detail_view

from aproducts.views import aproduct_upload,product_list_view,product_detail_view

# from huaweiproducts.views import huaweiproduct_upload,product_list_view,product_detail_view





from carts.views import cart_home

from accounts.views import login_page,register_page, guest_register_view
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from .views import home_page,about_page,contact_page,cart_page

urlpatterns = [
    url(r'^$',home_page, name="home"),
    url(r'^about/$',about_page, name="about"),
    url(r'^contact/$',contact_page, name="contact"),
    url(r'^login/$',login_page, name="login"),
    url(r'^checkout/address/create/$', checkout_address_create_view, name="checkout_address_create"),
    url(r'^checkout/address/reuse/$', checkout_address_reuse_view, name="checkout_address_reuse"),
    url(r'^register/guest/$', guest_register_view, name="guest_register"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^cart/$',cart_home, name="cart"),
    url(r'^cart/', include(("carts.urls", "carts"), namespace="cart")),
    url(r'^register/$',register_page, name="register"),
    url(r'^bootstrap/$',TemplateView.as_view(template_name="bootstrap/example.html")),
    url(r'^products/',include(("products.urls","products"), namespace = "products")),
    url(r'^product/', include(("product.urls", "product"), namespace="product")),
    url(r'^accproduct/', include(("product.urls", "product"), namespace="accproduct")),
    url(r'^accessories/', include(("accessories.urls", "accessories"), namespace="accessories")),
    url(r'^pproducts/', include(("pproducts.urls", "pproducts"), namespace="pproducts")),
    url(r'^aproducts/', include(("aproducts.urls", "aproducts"), namespace="aproducts")),
    # url(r'^huaweiproducts/', include(("huaweiproducts.urls", "huaweiproducts"), namespace="huaweiproducts")),
    url(r'^1_GB_Mobiles/', include(("One_GB_Mobiles.urls", "One_GB_Mobiles"), namespace="One_GB_Mobiles")),
    url(r'^Two_GB_Mobiles/', include(("Two_GB_Mobiles.urls", "Two_GB_Mobiles"), namespace="Two_GB_Mobiles")),
    url(r'^Three_GB_Mobiles/', include(("Three_GB_Mobiles.urls", "Three_GB_Mobiles"), namespace="Three_GB_Mobiles")),

    # url(r'^ratings/', include(('star_ratings.urls', "star_ratings"), namespace='ratings' )),

    url(r'^FivektoTenk/', include(("FivektoTenk.urls", "FivektoTenk"), namespace="FivektoTenk")),
    url(r'^TenktoTwentyk/', include(("TenktoTwentyk.urls", "TenktoTwentyk"), namespace="TenktoTwentyk")),
    url(r'^TwentyktoThirtyk/', include(("TwentyktoThirtyk.urls", "TwentyktoThirtyk"), namespace="TwentyktoThirtyk")),

    url(r'^FiveMPMobile/', include(("FiveMPMobile.urls", "FiveMPMobile"), namespace="FiveMPMobile")),
    url(r'^EightMPMobile/', include(("EightMPMobile.urls", "EightMPMobile"), namespace="EightMPMobile")),
    url(r'^TwelveMPMobile/', include(("TwelveMPMobile.urls", "TwelveMPMobile"), namespace="TwelveMPMobile")),


    url(r'^search/', include(("search.urls", "search"), namespace="search")),
    url(r'^searchprice/', include(("searchprice.urls", "searchprice"), namespace="searchprice")),
    url(r'^searchram/', include(("searchram.urls", "searchram"), namespace="searchram")),
    url(r'^searchknowledge/', include(("searchknowledge.urls", "searchknowledge"), namespace="searchknowledge")),


    path('upload-csv/', product_upload, name="product_upload"),
    path('upload-apple-csv/', aproduct_upload, name="aproduct_upload"),
    # path('upload-huawei-csv/', huaweiproduct_upload, name="huaweiproduct_upload"),
    # path('upload-1GB-csv/', One_GB_Mobile_product_upload, name="One_GB_Mobile_product_upload"),

    # url(r'^featured/$', ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)$', ProductFeaturedDetailView.as_view()),
    # url(r'^products/$',ProductListView.as_view()),
    # url(r'^products-fbv/$',product_list_view),
    # url(r'^products/(?P<pk>\d+)/$',ProductDetailView.as_view()),
    # url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
    # url(r'^products-fbv/(?P<pk>\d+)/$',product_detail_view),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
