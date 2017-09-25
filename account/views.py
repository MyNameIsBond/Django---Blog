from django.shortcuts           import render , redirect
from django.http                import HttpResponse
from .forms                     import Log_in_form , UserRegisterForm
from django.contrib.auth.forms  import UserCreationForm
from django.contrib             import messages
from django.contrib.auth        import ( 
                                        authenticate,
                                        get_user_model,
                                        login,
                                        logout,)

def profile(request):
    world = "HEEEEEEEY!"
    content = {
        "hello" : "Hello world",
        "world" : world,
    }
    return render (request, "profile.html", content)
# ----------------------------->Log in< -----------------------------#
def log_in(request):
    title = "Login"
    form = Log_in_form(request.POST or None)
    content = {
        "title" : title ,
        "form" : form
        }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login (request, user)
        print(user)
        messages.success(request,"You have logged in.")
        return redirect( "base" )
    return render (request, "log_in.html", content)

def log_out(request):
    logout(request)
    return redirect("base")
def register(request):
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user     = form.save(commit=False)
        password = form.cleaned_data.get("password1")
        user.set_password(password)
        user.save() 
        new_user = authenticate(username=user.username, password=password)
        login(request,new_user)
        messages.success(request,"Welcome, %s , enjoy." %request.user)
        print(request.user)
        return redirect("base")
    content = {
        "title" : title ,
        "form" : form
    }
    return render (request, "log_in.html", content)


def edit_profile(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(profile)
    else:
        form = UserCreationForm(instance=request.user)
        content = {"form":form}
        return (request, "edit",content)
        
