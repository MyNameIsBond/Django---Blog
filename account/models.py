from django.db                  import models
from django.db                  import models
from django.contrib.auth.models import User
from django.db.models.signals   import post_save
from django.dispatch            import receiver
from django.conf                import settings



class Profile(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio         = models.TextField(max_length=500, blank=True)
    email       = models.EmailField(blank=True)
    location    = models.CharField(max_length=30, blank=True)
    birth_date  = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user