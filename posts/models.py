from django.db                  import models
from django.urls                import reverse
from django.conf                import settings
from account.models             import Profile
from django.utils.text          import slugify
from django.db.models.signals   import pre_save
from django.contrib.auth.models import User

def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)

class Posts(models.Model):
    user     =   models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)   
    slug         = models.SlugField(unique=True)
    title        = models.CharField(max_length=60, blank=False, null=True)
    post         = models.TextField()
    pub_date     = models.DateField(null=True,auto_now_add=True)
    updated      = models.DateField(null=True, auto_now_add=True)
    image        = models.ImageField(null=True, blank=True,
                    upload_to=upload_location, 
                    width_field="width_field",
                    height_field="height_field")
    width_field  = models.IntegerField(default=0) 
    height_field = models.IntegerField(default=0)

    
    def __str__ (self):
        return u"%s %s" % (self.title, self.pub_date)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs= {"slug": self.slug})
        

    class Meta:
        ordering = ["-pub_date"]


def create_slug(instance, new_slug = None):
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug
    qs = Posts.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()

    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    print (slug)
    return slug

def pre_save_posts_receiver(sender ,instance ,*args, **kwargs ):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_posts_receiver,sender=Posts)


