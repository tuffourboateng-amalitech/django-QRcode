from django.shortcuts import render

# Create your views here.
def QRview(request):
    return render(request, 'QRstatic/QR.html')