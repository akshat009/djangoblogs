from django.shortcuts import render,  HttpResponse

from django.template.loader import get_template

from .forms import ContactForm


def home(request):
    return render(request, 'index.html')


def about(request):

    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
         full_name = form.cleaned_data['full_name']
         email= form.cleaned_data['email']
        #print(full_name, email)
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def example(request):
    context = {"title":  "Example"}
    template_name = "index.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))







