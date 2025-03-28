from django.shortcuts import render,redirect
from django.db.models import Prefetch
from category.models import Category, Region
from product.models import Product, ProductImage
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('main')
            else:
                form.add_error(None,'Login yoki parol notogri')
        else:
            form = LoginForm()
    return render(request,'login.html',{'form':form})    
def logout_view(request):
    logout(request)  
    request.session.flush()
    return redirect('main')
def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		else:
			form.add_error(None,"Toliq va hatolarsiz toldiring!")
	context = {
     'form':form
		}
	return render(request,'register.html',context)			

def main(request):
    # Barcha kategoriyalarni olish
    

    # Asosiy kategoriyalarni olish
    categories = Category.objects.filter(is_main=True)

    # Asosiy rasmlar bilan birga mahsulotlarni olish
    products = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.filter(is_main=True), to_attr='main_images')
    )
    region = Region.objects.all()

    print(products)

    # Kontekstni shakllantirish
    ctx = {
        "categories": categories,
        "products": products,
        "regions": region,
        
    }

    return render(request, 'index-2.html', ctx)
