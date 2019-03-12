from django.shortcuts import render
from .forms import ProductForm
from .models import Product
from django.http import HttpResponse
def insert(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            p1=Product(pid=form.cleaned_data['pid'],
                       pname=form.cleaned_data['pname'],
                       pcost=form.cleaned_data['pcost'],
                       pmfd=form.cleaned_data['pmfd'],
                       pexpdt=form.cleaned_data['pexpdt'])
            p1.save()
            return HttpResponse("data inserted successfully")
    else:
        form = ProductForm()
        return render(request,'input.html',{'form': form})

