from django.shortcuts import render

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

        messages.success(request,"User is created !")

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


