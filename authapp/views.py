from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import time
from .models import *

# Create your views here.

def home(request):
    return render(request, 'index.html')



def signup(request):
    if request.method == 'POST':
        user = request.POST.get('usernumber')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')


        if len(user) != 10:
            messages.warning(request,"Phone number must be 10 digits")
            return redirect('/signup')


        if pass1 != pass2:
            messages.info(request,"Please confirm your password")
            return redirect('/signup')
        
        if User.objects.filter(username=user).exists():
            messages.warning(request,"User is already exist")
            return redirect('/signup')


        if User.objects.filter(email=email).exists():
            messages.warning(request,"Email is already exist")
            return redirect('/signup')


        myuser = User.objects.create_user(user,email,pass1)
        myuser.save()

        messages.success(request," Registration Successfull")

        return redirect('/login')
    return render(request,'signup.html')

def loginpage(request):
    if request.method=='POST':
        user = request.POST.get('usernumber')
        pass1 = request.POST.get('pass1')
        myuser = authenticate(request, username=user,password=pass1)
        if myuser is not None:
            login(request,myuser)
            return redirect('/')
        else:
            messages.error(request," User invalid ")
    return render(request,'login.html')


def logoutpage(request):
    logout(request)
    return redirect('/')




def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        desc = request.POST.get('desc')

        if len(phonenumber) != 10:
            messages.warning(request,"Please end valid phone number")
            return redirect('/contact')
        myquery = Contact(name=name,email=email,phonenumber=phonenumber,description=desc)
        myquery.save()
        messages.info(request,"Thanks for contacting us we will get back you soon")
        return redirect('/contact')
    return render(request, 'contact.html')

@login_required(login_url='login')
def enroll(request):
    membership = MembershipPlan.objects.all()
    selecttrainer = Trainer.objects.all()
    context = {"membership": membership,"selecttrainer": selecttrainer}

    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        member = request.POST.get('member')
        trainer = request.POST.get('trainer')
        address = request.POST.get('address')

        if Enrollment.objects.filter(Email=email )or Enrollment.objects.filter(PhoneNumber=phonenumber).exists():
            messages.warning(request,"Already member Plz signin")
            return redirect('/enroll')

        myquery = Enrollment(
            FullName=fullname,
            Email=email,
            PhoneNumber=phonenumber,
            Gender=gender,
            DOB=dob,
            SelectMembershipplan=MembershipPlan.objects.get(id=member),
            SelectTrainer=Trainer.objects.get(id=trainer),
            Address=address,
            )
        
        myquery.save()
        messages.success(request,"Enrollment successfull ")
        return redirect('/enroll')

    return render(request,'enroll.html',context)


@login_required(login_url='login')
def profile(request):
    user = request.user.username
    posts = Enrollment.objects.filter(PhoneNumber=user)
    #print(posts.count())
    #print(posts)
    context = {"posts": posts}
    return render(request,'profile.html',context)

def gallery(request):
    posts = Gallery.objects.all()
    context = {'posts': posts}
    
    return render(request,'gallery.html',context)


