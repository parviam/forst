from django.shortcuts import render
from django.conf import settings
def index(request):
    template_data = {}
    template_data['title'] = 'Forst'
    return render(request, 'home/index.html', {
        'template_data': template_data
    })
def about(request):
    template_data = {}
    template_data['title'] = 'About'
    return render(request, 'home/about.html', {
        'template_data': template_data
    })
def maps(request):
    template_data = {}
    template_data['title'] = 'Maps'
    return render(request, 'home/maps.html', {
        'template_data': template_data,
        'maps_api_key': settings.MAPS_API_KEY
    })

# Create your views here.
