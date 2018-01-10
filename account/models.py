from django.db                  import models
from django.db.models.signals   import post_save , pre_save
from django.contrib.auth.models import User
from django.dispatch            import receiver
from django.conf                import settings
from django.urls                import reverse
from django.utils.text          import slugify





def upload_location(instance,filename):
    return "%s/%s" %(instance.user.username,filename)



class Profile(models.Model):

    user        = models.OneToOneField(User,on_delete=models.CASCADE)
    user_url    = models.SlugField(unique=True)
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


    def get_absolute_user(self):
      return reverse("account:profile", kwargs ={"user_url": self.user_url})


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):

  if created:
      Profile.objects.create(user=instance)
  instance.profile.save()



def create_slug(instance, new_slug = None):
    user_url = slugify(instance.user)

    if new_slug is not None:
        user_url = new_slug
    qs = Profile.objects.filter(user_url=user_url).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" %(user_url, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return user_url

def pre_save_Profile_receiver(sender ,instance ,*args, **kwargs ):
    if not instance.slug:
        instance.user_url = create_slug(instance)

pre_save.connect(pre_save_Profile_receiver, sender=Profile)








