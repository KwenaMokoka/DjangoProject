from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home_view(request):
    return render(request, 'home.html')

@login_required
def contact_us_view(request):
    return render(request, 'contact_us.html')

@login_required
def about_us_view(request):
    return render(request, 'about_us.html')