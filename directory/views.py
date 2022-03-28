from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from directory.models import contact, user
from werkzeug.security import check_password_hash ,generate_password_hash
# Create your views here.


def register(request):
    if request.method=="POST":
        name=request.POST.get('user')
        email=request.POST.get('email')
        phone =request.POST.get('phone')
        password =request.POST.get('password')
        hash=generate_password_hash(password)
        e= user.objects.filter(email=email).exists()
        if e:
            return HttpResponse("Already User with this mail exists")
        else:
            Registed_user= user(name=name,phone_no=phone,email=email,password=hash)
            Registed_user.save()
        return redirect("/")
        
    else:
        return render(request,"register.html")

def login(request):
     if request.method=="POST":
         email=request.POST.get('email')
         password =request.POST.get('password')
         e= user.objects.filter(email=email).exists()
         if e:
             p = user.objects.get(email=email).password
             if check_password_hash(p,password):
                 request.session["login"]=1
                 request.session["email"]=email
                 return redirect("/homepage")
             else:
                 return HttpResponse("Password Not Matched")

         else:
            return HttpResponse("User doesnot exists")
        
     return render(request,"login.html")

def homepage(request):
    email= request.session["email"]
    name=user.objects.get(email=email).name
    id=user.objects.get(email=email).id
    if (request.method=="POST"):
        fname=request.POST.get('name')
        lname=request.POST.get('lname')
        phone=request.POST.get('phone')
        Address=request.POST.get('address')
        # img=request.POST.get('img')
        cont = contact(fname=fname,lname=lname,phone=phone,Address=Address,user_id=id)
        cont.save()

    return render(request,"homepage.html",{"name":name.capitalize()})

def all_contact(request):
    email= request.session["email"]
    name=user.objects.get(email=email).name
    I=user.objects.get(email=email).id
    all_cont=contact.objects.filter(user_id=I).all()
    # print("============",all_cont)
    return render(request,"all_contact.html",{"name":name.capitalize(),"all_cont":all_cont})

from django.db.models import Q
def update(request):
    # email= request.session["email"]
    # name=user.objects.get(email=email).name
    # print("-----------------")
    if (request.method=="POST"):
        if (request.POST.get("name")==None):
            fname=request.POST.get('fname')
            print(fname)
            lname=request.POST.get('lname')
            phone=request.POST.get('phone')
            Address=request.POST.get('Address')
            ids=request.POST.get('id')
            print(ids,"----------------------")
            t = contact.objects.get(id=ids)
            t.fname = fname
            t.lname = lname
            t.phone = phone
            t.Address = Address
            t.save()
            return redirect("/")
        else:

            query = request.POST.get('name','')
            if query:
                    queryset = (Q(fname__icontains=query))
                    results = contact.objects.filter(queryset).distinct()
            else:
                results = []
            return render(request, 'update.html', {'results':results})
    else:
        return render(request,"update.html")