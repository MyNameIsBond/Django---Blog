from django                     import forms
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth        import ( 
                                         authenticate,
                                         get_user_model,
                                         login,
                                         logout,)
User = get_user_model()

class Log_in_form(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args, **kwargs):
        username  = self.cleaned_data.get("username")
        password  = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username,password=password )
            if not user:
                raise forms.ValidationError("This User Does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorect Password")
            if not user.is_active:
                raise forms.ValidationError("This User is no longer active")
        return super(Log_in_form,self).clean(*args,**kwargs)

class UserRegisterForm(UserCreationForm):
    """Form definition for UserRegister."""
    email       = forms.EmailField(label="Email Adress")
    email2      = forms.EmailField(label="Comfirm Email")
    # password    = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        """Meta definition for UserRegisterform."""
        model  = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  "email2",
                  "password1",
                  "password2" )

    def clean_email2(self):
        email2  = self.cleaned_data.get("email2")
        email   = self.cleaned_data.get("email")
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This Mail has already been registered")
        return email