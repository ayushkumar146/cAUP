from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

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

# Create your views here.
