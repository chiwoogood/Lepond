from django.shortcuts import render

# Create your views here.
def items(request):
    return render(request,'shop/items.html')

def details(request):
    return render(request, 'shop/details.html')