from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact


# Create your views here.
def contact(request):
    if request.method == 'POST':
        title = request.POST['machine']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact = Contact(title=title, username=username, phone=phone, email=email, message=message )
        contact.save()
        messages.success(request, 'Thanx for contact us ')
        return redirect('/machines/')