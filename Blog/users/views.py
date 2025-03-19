from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from . import forms
from django.contrib.auth import authenticate,login,logout
from .forms import createuser,loginform,EditProfile
from django.contrib import messages
from .models import User,Profile
from django.contrib.auth.decorators import login_required
# Create your views here.


def form(req):
    form1 = forms.createuser()
    return render(req, "form.html", {"forms": form1})

def signup(req):
    if req.method == "POST":
        form = createuser(req.POST)
        if form.is_valid():
            print("form is valid")
    return HttpResponse("signup page")

def signup_view(req):
    if req.user.is_authenticated:
        return redirect('core:home')
        # return redirect('users:form')
    if req.method == "POST":
        form = forms.createuser(req.POST)
        if form.is_valid():
            user1 = form.save()
            login(req,user1)
            messages.success(req,"Account created successfully")
            return redirect('core:home')
            # return redirect('users:form')
    else:
        form = forms.createuser()
        return render(req,'users/signup.html',{'form':form}) 

def login_view(req):
    if req.user.is_authenticated:
        return redirect('core:home')
        # return redirect('users:form')
    if req.method == "POST":
        form = loginform(req.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(email=email,password=password)
            if user:
                login(req,user)
                messages.success(req,"login successful")
                return redirect('core:home')  
                # return redirect('users:form') 
            else:
                messages.error(req,"email or passowrd is incorrect")
    else:
        form = loginform()
        return render(req,'users/login.html',{'form':form})

def logout_view(req):
    logout(req)
    return redirect('core:login')

@login_required

# def profile(req,username):
#     user  = get_object_or_404(User,username=username)
#     profile = get_object_or_404(profile,user=user)
#     return render(req,'users/profile.html',{'profile':profile,'user':user})

def profile(req):
    # user  = get_object_or_404(User,username=username)
    user = req.user
    profile = get_object_or_404(Profile,user=req.user)
    # print(profile)
    return render(req,'users/profile.html',{'profile':profile,'user':user})
    # return render(req,'users/profile.html')



@login_required

def edit_profile(req):
    if req.method == "POST":
        form = EditProfile(req.user.username,req.POST,req.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            about = form.cleaned_data['about']
            image = form.cleaned_data['photo']

            user = User.objects.get(id = req.user.id)
            user.username = username
            user.save()
            profile = Profile.objects.get(user = user)
            profile.about = about
            if image:
                profile.photo = image
            profile.save()
            messages.success(req,"profile updated successfully")

            return redirect('users:profile',username = user.username)
    else:
        form = EditProfile(req.user.username)
        return render(req,'users/editprofile.html',{'form':form})

            

