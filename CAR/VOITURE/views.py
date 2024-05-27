from django.shortcuts import render
from .forms import UserCreationForm

# Create your views here.
def acceuil(request):
    return render(request,'acceuil.html')

def Login(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return acceuil('acceuil.html')
    else:
        form = UserCreationForm() 
    return render(request,'Login.html')

def register(request):
    return render(request,'register.html')

def aboutus(request):
    return render(request,'aboutus.html')

def reserver(request):
    return render(request,'reserver.html')




