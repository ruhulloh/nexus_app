from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
from django.db.models import *
from category.models import *
from .models import *

def category_products(request):
	product = Product.objects.prefetch_related(Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images'))
	# product = Product.objects.all()
	paginator  = Paginator(product,2)
	pag_req = request.GET.get("page")
	page_obj =  paginator.get_page(pag_req)
	context  = {
		'products':page_obj,
		# 'images':product_images,
	}
	return render(request,'category.html',context)	

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    product_images = ProductImage.objects.exclude(is_main=False)

    ctx = {
       'product':product,
		'images':product_images,

    }
    return render(request, 'detail.html', ctx)