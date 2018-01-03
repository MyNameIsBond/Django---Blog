from django.db                  import models
from django.db.models.signals   import post_save , pre_save
from django.contrib.auth.models import User
from django.dispatch            import receiver
from django.conf                import settings
from django.urls                import reverse




def upload_location(instance,filename):
    return "%s/%s" %(instance.user.username,filename)



class Profile(models.Model):

    user        = models.OneToOneField(User,on_delete=models.CASCADE)
    bio         = models.TextField(max_length=500, blank=True)
    location    = models.CharField(max_length=30, blank=True)
    birth_date  = models.DateField(null=True, blank=True)
    prof_image  = models.ImageField(null=True, blank=True,
                  upload_to=upload_location, 
                  width_field="width_field",
                  height_field="height_field")
    width_field  = models.IntegerField(default=0) 
    height_field = models.IntegerField(default=0)


    def __str__(self):
      return self.user.username


    def get_absolute_url(self):
      return reverse("account:profile")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

  if created:
      Profile.objects.create(user=instance)
  instance.profile.save()











