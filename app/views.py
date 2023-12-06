from django.shortcuts import render

# Create your views here.
def parrent(request):
    return render(request,'parrent.html')


def child(request):
    return render(request,'child.html')