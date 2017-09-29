from django.shortcuts           import render , redirect
from django.http                import HttpResponse
from django.contrib.auth.forms  import (UserCreationForm ,PasswordChangeForm, UserChangeForm)
from django.contrib             import messages
from django.contrib.auth        import (authenticate,
                                        update_session_auth_hash,
                                        get_user_model,
                                        login,
                                        logout,)
from .forms                     import Log_in_form,UserRegisterForm,EditProfile
# ---------------------------- >Profile View< ----------------------------#
def profile(request):
    world = "HEEEEEEEY!"
    content = {
        "hello" : "Hello world",
        "world" : world,
    }
    return render (request, "profile.html", content)


# -------------------------- >Log in , Log out< --------------------------#
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
        messages.success(request,"%s, have logged in." %request.user)
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


# ---------------------> Change Password / Edit Profile <---------------------

def edit_password(request):
    content = {"title": "%s, Change Password" %request.user}
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            messages.success(request,"Your password, %s, have been saved." %request.user)
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect("account:profile")
        else:
            messages.error(request,"Something went wrong, try again.")
            redirect("edit.html")
    else:
        form = PasswordChangeForm(user=request.user)
        content = {"form":form, "title":"Change Password"}
        return render(request,"edit.html",content)
    return render(request,"edit.html")
                

def edit_profile(request):
    content = { "title": "Change Profile" }
    if request.method == "POST":
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request,"Your changes, %s, have been saved." %request.user)
            form.save()
            return redirect("account:profile")
        else:
            messages.success(request,"Your changes, %s, have been saved." %request.user)
            
    else:
        form = EditProfile(instance=request.user)
        content = {"form":form, "title": "Edit Profile"}
        return render(request, "edit.html",content)
    return render(request, "edit.html")