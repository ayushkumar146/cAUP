from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from .forms import ContactForm
from django.urls import reverse

def contact_view(request, user_id):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email to the host/owner
            send_mail(
                subject,
                f'Message from {fullname} ({email}):\n\n{message}',
                email,  # User's email as the sender
                ['ayush.kumardas146@gmail.com'],  # Host/owner email
                fail_silently=False,
            )

            # Add a success message
            messages.success(request, 'Your message has been sent successfully!')

            # Redirect back to the contact page with user ID
            return redirect(reverse('contact-page', args=[user_id]))

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def user_homepage(request, user_id):
    user = get_object_or_404(User, id=user_id)
    # Fetch any other data you need for the user
    template = loader.get_template('user_homepage.html')
    context = {
        'user': user,
        # Include other user-specific data here
    }
    print(user)
    return HttpResponse(template.render(context,request))

def contact_page(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        return contact_view(request, user_id)  # Pass user_id to contact_view
    else:
        return render(request, 'contact.html', {'user': user})



# Create your views here.
