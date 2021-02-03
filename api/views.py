from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from .serializers import ProductSerializer
from rest_framework.renderers import JSONRenderer
from api.forms import ProductrForm
from django.views.generic import CreateView
# Create your views here.

def index(request):
    if request.method == "POST":
        form = ProductrForm(request.POST,request.FILES)
        # print(form)
        if form.is_valid():
            form.save()
            # return render(request, "index.html", context)

    else:
        form = ProductrForm()
    # print(form)
    context = {'fom':form}
    return render(request, "product.html", context)


def product_api(request):
    if request.method == "GET":
        model = Product.objects.all()
        serializer_data = ProductSerializer(model, many=True)
        jsondata = JSONRenderer().render(serializer_data.data)
        # print(model)

        return HttpResponse(jsondata, content_type="application/json")

        