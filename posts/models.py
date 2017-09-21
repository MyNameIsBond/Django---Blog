from django.db                  import models
from django.core.urlresolvers   import reverse
from account.models             import Profile
from django.contrib.auth.models import User
from django.conf                import settings



class Posts(models.Model):
    # user     =   models.ForeignKey(Profile)
    title    =   models.CharField(max_length=30, blank=False, null=True)
    post     =   models.TextField()
    pub_date =   models.DateField(null=True,auto_now_add=True)
    updated  =   models.DateField(null=True, auto_now_add=True)
    
    def __str__ (self):
        return u"%s %s" % (self.title, self.pub_date)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs= {"id": self.id})

    class Meta:
        ordering = ["-pub_date"]
