from django.shortcuts import render, redirect

from application.forms import CustomerForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

# Contact page
def contact(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('index')
    else:
        form = CustomerForm()
    return  render(request,'contact.html',{'form':form})