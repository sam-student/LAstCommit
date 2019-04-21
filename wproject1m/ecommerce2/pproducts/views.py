import csv, io
# from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required



# Create your views here.
from carts.models import Cart
from .models import P_Product

class ProductFeaturedListView(ListView):
    template_name = "pproducts/list.html"

    def get_queryset(self, *args, **kwargs ):
        request = self.request
        return P_Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = P_Product.objects.all().featured()
    template_name = "pproducts/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return product.objects.featured()

class ProductListView(ListView):
    #queryset = product.objects.all()
    template_name = "pproducts/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args ** kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs ):
        request = self.request
        return P_Product.objects.all()


def product_list_view(request):
    queryset = P_Product.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, "pproducts/list.html", context)

class ProductDetailSlugView(DetailView):
    queryset = P_Product.objects.all()
    template_name = "pproducts/detail.html"

    def get_context_data(self,*args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get("slug")
        #instance = get_object_or_404(product , slugs=slug, active=True)

        try:
            instance = P_Product.objects.get(slug=slug)
        except P_Product.DoesNotExist:
            raise Http404("Not found..")
        except P_Product.MultipleObjectsReturned:
            qs = P_Product.objects.filter(slug=slug)
            instance=qs.first()
        except:
            raise Http404("Uhmm")

        return instance

class ProductDetailView(DetailView):
    #queryset = product.objects.all()
    template_name = "pproducts/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context

    def get_object(self, *args, **kwargs):
        request =self.request
        pk = self.kwargs.get("pk")
        instance = P_Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("product doesn't exist")
        return instance

    # def get_queryset(self, *args, **kwargs ):
    #     request = self.request
    #     pk = self.kwargs.get("pk")
    #     return product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **kwargs):
        #instance = product.objects.get(pk=pk, featured=True)
        #instance = get_object_or_404(product, pk=pk , featured=True)
    # try:
    #     instance =product.objects.get(id=pk)
    # except product.DoesNotExist:
    #     print('no products here')
    #     raise Http404("product does,not exist")
    # except:
    #     print("huh?")

    instance = P_Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404("product doesn't exist")
    # print(instance)
    #
    # qs = product.objects.filter(id=pk)
    # if qs.exists() and qs.count() ==1:
    #     instance = qs.first()
    # else:
    #     raise Http404("product does,not exist")

    context = {
        "object": instance
    }
    return render(request, "pproducts/detail.html", context)




@permission_required('admin.can_add_log_entry')
def product_upload(request):
    template = 'product_upload.html'

    prompt = {
        'order': 'Order of our csv should be like your model'
    }


    if request.method == 'GET':
        return render(request, template , prompt)

    csv_file= request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,"this is not a csv file")

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=",", quotechar="|" ):
       _, created = P_Product.objects.update_or_create(
            title = column[0],
            slug=column[1],
            price=column[2],
            sound=column[3],
            memory=column[4],
            camera=column[5],
            connectivity=column[6],
            diplay=column[7],
            processor=column[8],
            color=column[9],
            image =column[10],
            Review_count=column[11],
            Average_Rating=column[12],

        )

    context ={}
    return render(request, template, context)


