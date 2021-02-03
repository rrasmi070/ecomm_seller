from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.core.files.storage import FileSystemStorage
from seller.models import Register
from seller.forms import RegisterForm
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    if request.method == "POST":
        form = RegisterForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            # return render(request, "index.html", context)

    else:
        form = RegisterForm()
    # print(form)
    context = {'form':form}
    return render(request, "index.html", context)

