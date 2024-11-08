from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# register view function
def register(request):
    form = None
    # if the request method is POST
    if request.method == "POST":
        # instance of UserRegisterForm with post data
        form = UserRegisterForm(request.POST)
        # if form data is valid
        if form.is_valid():
            #save the user in db
            form.save()
            username = form.cleaned_data.get("username") 
            # show a custom message
            messages.success(request, f'Your account has been created!')
            # redirect to blog home page
            return redirect("login")
    # if the method is not POST
    else:
        # instance of UserRegisterForm with empty data
        form = UserRegisterForm()    
    # passing form as a context
    return render(request, "users/register.html", {"form": form})

# profile view function with protected route
# you cannot access this route until you log in
@login_required
def profile(request):
    # if the request method is POST
    if request.method == "POST":
        # create an instance of user form with provided data
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # create an instance of profile form with provided data
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        # if both the forms are valid
        if u_form.is_valid() and p_form.is_valid():
            # save the data provided in form
            u_form.save()
            p_form.save()
            # show a custom message
            messages.success(request, f'Your account has been updated!')
            # redirect to profile page
            return redirect("profile")
    # if the method is not POST
    else:
        # create an instance of user form with exisiting data
        u_form = UserUpdateForm(instance=request.user)
        # create an instance of profile form with existing data
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, "users/profile.html", context)
        
    
  
    
    