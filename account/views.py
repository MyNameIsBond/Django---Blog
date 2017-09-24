from django.shortcuts       import render , redirect
from django.http            import HttpResponse
from .forms                 import Log_in_form , UserRegisterForm
from django.contrib.auth.forms  import UserCreationForm
from django.contrib         import messages
from django.contrib.auth    import ( 
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
        password = form.cleaned_data.get("password")
        # user.set_password(password)
        user.save() 
        new_user = authenticate(username=user.username, password=password)
        print(user.password)
        login(request,new_user)
        messages.success(request,"The User Has Been Created")
        return redirect("base")
        print(request.user)
    content = {
        "title" : title ,
        "form" : form
    }
    return render (request, "log_in.html", content)