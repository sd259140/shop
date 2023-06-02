# shoppinglyx
This is a Static DJango Shopping Website 
![alt text](https://github.com/geekyshow1/shoppinglyx/blob/main/Screenshots/Home.jpeg)
from .models import (Customer,Product,Orderplaced,Cart)

@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    list_display =['id','user','name','locality','city','zipcode','state']

@admin.register(Product)    
class ProductAdmin(admin.ModelAdmin):
    list_display =['id','title','selling_price','discounted_price','description','brand',' category','product_img']

@admin.register(Orderplaced)    
class orderplacedAdmin(admin.ModelAdmin):
    list_display =['id','user','product','quantity']

@admin.register(Cart)    
class cartAdmin(admin.ModelAdmin):
    list_display =['id','user','customer','product','quantity','ordered_date','status']        

    