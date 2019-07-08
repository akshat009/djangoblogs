from django.shortcuts import render,  HttpResponse, get_object_or_404
from .models import BlogPost


def details(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    return render(request, 'blog_details.html', context)


def index(request):
    qs = BlogPost.objects.all()
    context={'object_list': qs}
    return render(request, 'blogs.html', context)


def example(request):
    context = {"title":  "Example"}
    template_name = "index.html"
    template_obj= get_template(template_name)
    return HttpResponse(template_obj.render(context))







