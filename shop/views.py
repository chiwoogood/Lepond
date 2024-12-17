from django.shortcuts import render

# Create your views here.
def items(request):
    return render(request,'shop/items.html')