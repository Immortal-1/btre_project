from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import Contact
# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
                user_id = request.user.id
                has_contacted = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
                if has_contacted:
                        return redirect('/listings/'+listing_id)                        

        contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)

        contact.save()

        send_mail(
                'Property Listing Inquiry'
                'There has been an inquiry for '+ listing + '.Sign into admin panel for more info',
                'heymantu01@gmail.com',
                [realtor_email,'rightthing79@gmail.com'],
                fail_silently=False
        )

        return redirect('/listings/'+listing_id)