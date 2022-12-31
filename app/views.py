from django.shortcuts import render

# Create your views here.
def teja(request):
    d={'a':20,'b':19}
    return render(request,'bala.html',d)