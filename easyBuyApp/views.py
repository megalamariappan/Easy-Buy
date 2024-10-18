from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import products,card,payment,orders
# Create your views here.

def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_pw=request.POST.get('confirm_password')
        
        if password!=confirm_pw:
            messages.error(request,'Password do not Match')
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request,'Username already Exists')
            return redirect('signup')
        
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        messages.success(request,'Registration Successfull')
        return redirect('login')
    return render(request,'easybuy/signup.html')

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user_valid=authenticate(request,username=username,password=password)
        if user_valid is not None:
            login(request,user_valid)
            # messages.success(request,'Successfully Logged In')
            return redirect('index')
        else:
            messages.error(request,'Invalid Username or Password')
    return render(request,'easybuy/login.html')

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("/")

def index(request):
    product_dict={
        'mens_dress':products.objects.filter(category_name__category__iexact='mens collection'),
        'womens_dress':products.objects.filter(category_name__category__iexact='womens collection'),
        'mens_shoes':products.objects.filter(category_name__category__iexact='mens shoes collection'),
        'womens_shoes':products.objects.filter(category_name__category__iexact='womens shoes collection'),
    }
    return render(request,'easybuy/index.html',{
        'product_dict':product_dict,
        'index_path':request.path
        })

def productDetails(request,id):
    details=products.objects.get(id=id)
    return render(request,'easybuy/product_details.html',{'details':details,'details_path':request.path})

def add_to_cart(request,id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            product=products.objects.get(id=id)
            if not card.objects.filter(product=product,user=request.user).exists():
                card_s=card.objects.create(product=product,user=request.user, quantity=1)
                card_s.save()
                messages.success(request, 'Product successfully added to the cart')
                return redirect('productDetails', id=id)
               
            else:
                get_card = card.objects.get(product=product, user=request.user)
                get_card.quantity += 1
                get_card.save()
                messages.success(request, 'Product successfully added to the cart')
        else:
            messages.warning(request,'You have to log in to add the product')
            return redirect('login')
    return redirect('productDetails',id=id)

def cards(request):
    if request.user.is_authenticated:
        get_cards=card.objects.filter(user=request.user)
        tot_disc=0
        tot_dis=o_disc=0
        disc=0
        original=0
        tot_original=0
        if get_cards:
            for i in get_cards:
                o_disc+=i.product.discount_amount
                original+=i.product.original_price
                tot_original+=(i.product.original_price*i.quantity)
                if i.quantity>1:
                    tot_disc+=i.quantity
                
        one_disc=abs(original-o_disc)
        disc_amt=abs(tot_original-disc)
        if tot_disc:
            tot_dis=one_disc*tot_disc
        else:
            tot_dis=one_disc
        return render(request,'easybuy/card.html',{
            'tot_original':tot_original,
            'original':original,
            'get_cards':get_cards,
            'one_disc':one_disc,
            'disc_amt':disc_amt,
            'tot_disc':tot_dis,
            'card_path':request.path
            })
    else:
        return redirect("login")
    
def remove_card(request,id):
    get_cardid=card.objects.get(id=id)
    get_cardid.delete()
    return redirect('cards')

def order(request,id):
    if request.user.is_authenticated:
        pay_method=payment.objects.all()
        get_product=products.objects.get(id=id)
        if request.method == 'POST':
            quantity=request.POST.get('quantity')
            name=request.POST.get('name')
            email=request.POST.get('email')
            address=request.POST.get('address')
            payment_method=request.POST.get('payment_method')
            payment_s=payment.objects.get(id=payment_method)
            
            product_order=orders.objects.create(user=request.user,
                                                product_name=get_product,
                                                quantity=quantity,
                                                name=name,
                                                email=email,
                                                address=address,
                                                payments=payment_s
                                                )
            product_order.save()
            messages.success(request, 'Your Order is Successful')
            return redirect('productDetails',id=id)
        return render(request,'easybuy/order.html',{'get_product':get_product,'pay_method':pay_method,'order_paths':request.path})
    else:
        return redirect('login')
    
def showOrders(request):
    if request.user.is_authenticated:
        get_user=orders.objects.filter(user=request.user).first()
        order=orders.objects.filter(user=request.user)
        return render(request,'easybuy/show_orders.html',{'order':order,'get_user':get_user,'orderpath':request.path})
    else:
        return redirect('login')