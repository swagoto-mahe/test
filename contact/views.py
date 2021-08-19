from django.shortcuts import render
from .models import Contact
# Create your views here.

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['msg']
        print(name, email, msg)
        contact = Contact(name=name, email=email, msg=msg)
        contact.save()
    return render(request, 'contact.html')
