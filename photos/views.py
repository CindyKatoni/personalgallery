from django.shortcuts import render
from photos.models import Image

# Create your views here.

def photo_index(request):
    images = Image.objects.all()
    context = {
        'images':images
    }
    return render(request, 'photo_index.html', context)

