from django.shortcuts import render,HttpResponse
from user.models import Login
from django.http import JsonResponse
from user.models import Signup
from django.conf import settings
from django.core.mail import send_mail
import random
from django.contrib.auth.models import User 
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        # print(email,password)
        if Signup.objects.filter(email=email).exists():
            login = Login(email=email,password=password)
            login.save()
            messages.success(request,"Login successfully") 

        else:
            messages.warning(request,"Email is not register go to create accounct") 
        # subject = 'welcome to GFG world'
        # message = f'Hi User is created'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['kaadesh18001@gmail.com']
        # send_mail( subject, message, email_from, recipient_list )


    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        firstn = request.POST.get('first_name')
        lastn = request.POST.get('last_name')
        phone = request.POST.get('phone')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        if Signup.objects.filter(email=email).exists():
            messages.warning(request,"Email is already register go to login page")
        else:
        # print(firstn,lastn,phone,email,password)
            subject = 'Email varification'
            otp = random.randint(100000,999999)
            # print(otp)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail( subject, f"OTP for a email varifiaction of {email} : {otp}", email_from, recipient_list )
            return render(request,'verify.html',{'otp':otp,'firstn':firstn,'lastn':lastn,'phone':phone,'email':email,'password':password})
    return render(request,'signup.html')

@csrf_exempt
def verify(request):
    if request.method=='POST':
        userotp =request.POST.get('otp')
        firstn =request.POST.get('firstn')
        lastn =request.POST.get('lastn')
        phone =request.POST.get('phone')
        email =request.POST.get('email')
        password =request.POST.get('password')

        form = Signup(first_name=firstn,last_name=lastn,phone=phone,email=email,password=password)
        form.save()
        messages.success(request,"Email verify successfully Go for login")


        print(userotp)
    return JsonResponse({'data':'hello'},status=200)
    