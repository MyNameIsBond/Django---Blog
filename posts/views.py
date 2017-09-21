from django.shortcuts import render , get_object_or_404 , redirect
from .forms           import PostForm
from .models          import Posts
from django.http      import HttpResponseRedirect 
from django.contrib   import messages




def home(request):
    if 'search' in request.GET:
        search = request.GET['search']
        if not search:
            posts = Posts.objects.none()
            return render(request,"search.html",{"posts":posts,"query":search})
        else:
            posts = Posts.objects.filter(title__icontains=search)
            return render(request,"search.html",{"posts":posts,"query":search})
    queryset = Posts.objects.all()
    if request.user.is_authenticated():
        hello = {
                "title" : "I know who you are, Tony",
                "msg":"Hello World of django yeeeeeee!",
                "objectlist" : queryset,}
    else:
        hello = {
                "title" : "I have no clue who you are, please sign up",
                "msg":"Hello World of django yeeeeeee!",
                "objectlist" : queryset,}
    return render (request,"index.html",hello)

def detail(request, id):
    """ Post Preview """ 
    instance = get_object_or_404(Posts, id=id)
    title = "Detail View"
    context = {
        "title" : instance.title,
        "instance" : instance
    }

    return render(request,"detail_view.html", context)

# >--------------------------- Post's Action -----------------------------------<
def create_post(request):
    """ This creates post """
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Post has been Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        context = {
            "form" : form,
        }
        return render(request, "create_post.html", context)


def update_post(request, id=None):
    """ this updates an already created post """

    instance = get_object_or_404(Posts, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Post has been updated")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title" : instance.title,
        "instance" : instance,
        "form" : form
    }
    return render(request, "create_post.html", context)

def delete_post (request, id=None):
    instance = get_object_or_404(Posts, id = id)
    instance.delete()
    messages.success(request," Post has been deleted")
    return redirect("base")


#----------------------------------- Search -----------------------------------#
def search(request):
    if 'search' in request.GET:
        search = request.GET['search']
        if not search:
            posts = Posts.objects.none()
            return render(request,"search.html",{"posts":posts,"query":search})
        else:
            posts = Posts.objects.filter(title__icontains=search)
            title = search
            return render(request,"search.html",{"posts":posts,"query":search,"title":title})
    return render(request,"search.html")