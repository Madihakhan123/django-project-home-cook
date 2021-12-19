from django.shortcuts import render , HttpResponse ,redirect, get_object_or_404 
from datetime import datetime
from home.models import contact
from shop.models import product,Order
#from shop.models import Orders
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages #import messages
from math import ceil


#from .forms import contactform

# Create your views here.
def index(request):
    context={
        "variable1": "Madiha is a good girl. Trust ME, She is.",
        "variable2": "Antara is a very very bad girl. Anatra 24 hours keep screeming at me :("
    }
    products = product.objects.all()
    print(products)
    n = len(products)
    nslides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nslides,'range':range(nslides),'product':products}
    return render(request, 'index.html',params)

def searchmatch(query, item):
    if query in item.desc.lower() or query in item.product_name.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    products = product.objects.all()
    prod = [item for item in products if searchmatch(query , item)]
    print(prod)
    n = len(prod)
    nslides = n//4 + ceil((n/4)-(n//4))
    if len(prod) != 0:
        params = {'no_of_slides':nslides,'range':range(nslides),'product':prod}

    if len(prod) ==0:
        params = {'msg': "please make sure to enter relevent search query. Sorry product not found."} 
           
    return render(request, 'index.html',params) 


def homemadefood(request):
    context={
        'var':'You can get best food here.'
    }
    products = product.objects.all()
    print(products)
    n = len(products)
    nslides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nslides,'range':range(nslides),'product':products}
    return render(request, 'homemadefood.html', params)

def about(request):
    return render(request, 'about.html')
     
def services(request):
    return render(request, 'services.html')

def con(request):
    context= {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
       # date = datetime.now
        con= contact(name=name, email= email, phone=phone, desc=desc)
        con.save()
        
    return render(request, 'contact.html',context)  

         
def handlesignup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        location =request.POST['location']


        #checking info 
        if len(username)>10:
            messages.error(request,"User name should be between 10 characters!")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"User name should contain only letters and numbers!")
            return redirect('home')

        if pass1!=pass2:
            messages.error(request,"Password doesn't match. Confirm again kindly.")
            return redirect('home')       


        
        #creating account and saving in database: 
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your Account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse('404- Not Found')  


def handlelogin(request):
    if request.method== 'POST':
        loginusername=request.POST['loginusername'] 
        loginpass=request.POST['loginpass']

        user = authenticate(username=loginusername, Password=loginpass)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request,"Something went wrong. Try Again Kindly.")
            return redirect('home')

    return HttpResponse('404-Not Found')   

def handlelogout(request):
    logout(request)
    messages.success(request,"Successfully Loggged Out")
    return redirect('home')


def tracker(request):
    return render(request,'tracker.html')

def checkout(request):
    return render(request,'checkout.html')        

def productview(request,id):
    #fetching products to show here :
    prod = product.objects.filter(id=id)
    print(prod)
    return render(request,'productview.html',{'product':prod[0]})

def viewrecipe(request,id):
    #fetching products to show here :
    prod = product.objects.filter(id=id)
    print(prod)
    return render(request,'viewrecipe.html',{'product':prod[0]})     

def order(request):
    if request.method == 'POST':
        #itemsjson = request.POST.get('itemsjson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip = request.POST.get('zip','')
        phone = request.POST.get('phone','')
        
        order= Order(name=name, email= email,address=address, city=city, state=state, zip=zip, phone=phone)
        order.save()

        thank = True
        id = Order.order_id

        return render(request, 'home.html',{'thank':thank, 'id':id})
    #return render(request,'checkout.html')       

    

