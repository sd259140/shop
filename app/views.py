from django.shortcuts import render
from django.views import View
from .models import Customer,Product,Orderplaced,Cart
from .forms import custumerRegisterForm,profileForm
from django.contrib import messages

def home(request):
 return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topwear=Product.objects.filter(category='TW')
        bottomwear=Product.objects.filter(category='BW')
        mobile=Product.objects.filter(category='M')
        laptop=Product.objects.filter(category='l')
        return render(request,'app/home.html',{'topwear':topwear,'bottomwear':bottomwear,'mobile':mobile,'laptop':laptop})

class product_detail(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})

 

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')



def address(request):
    add=Customer.objects.filter(user=request.user)


    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')



def mobile(request,data=None):
    if data==None:
        mobiles=Product.objects.filter(category='M')
    elif data == 'Redmi' or data == 'Samsung':
        mobiles=Product.objects.filter(category='M').filter(brand=data)
    return render(request,'app/mobile.html',{'mobiles':mobile})
def login(request):
 return render(request, 'app/login.html')

class customerregistration(View):
    def get(self,request):
        fm=custumerRegisterForm()
        return render(request, 'app/customerregistration.html',{'fm':fm})
    def post(self,request):
        fm=custumerRegisterForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.SUCCESS(request,'sucessfully register')
        return render(request, 'app/customerregistration.html',{'fm':fm})    
def checkout(request):
 return render(request, 'app/checkout.html')

class profileview(View):
    def get(self,request):
        form=profileForm()
        return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form=profileForm(request.POST)
        if form.is_valid():
            user=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            zipcode=form.cleaned_data['zipcode']
            state=form.cleaned_data['state']
            reg=Customer(user=user,name=name,locality=locality,city=city,zipcode=zipcode,state=state)
            reg.save()
            messages.success(request,'cogrtulation profile ctreated')
        return render(request, 'app/profile.html',{'form':form,'active':'btn-primary'})

