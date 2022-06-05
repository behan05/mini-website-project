from django.shortcuts import redirect, render
from .models import SignupTB

# Create your views here.
def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == "POST":
        nm = request.POST.get('name')
        em = request.POST.get('email')
        pwd = request.POST.get('pwd')
        db = SignupTB(name=nm,email=em,password=pwd)
        db.save()  
        return redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        em = request.POST.get('email')
        pwd = request.POST.get('pwd')
        try:
            db = SignupTB.objects.get(email=em,password=pwd)
        except SignupTB.DoesNotExist:
            return redirect('signup')
        else:
            request.session['uid']=db.id
            return render(request,'index.html')    
    return render(request,'login.html')    
            
def logout(request):
    if 'uid' in request.session:
        del request.session['uid']
        return redirect('login')
    return render(request, 'login.html')

def blog(request):
    if 'uid' in request.session:
        return render(request,'blog.html')
    else:
        return redirect('login')
    
def contact(request):
    if 'uid' in request.session:
        return render(request,'contact.html')
    else:
        return redirect('login')  
    
def Support(request):
    return render(request,'Support-blog1.html')     