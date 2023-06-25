from django.shortcuts import render
from django.core import serializers
from part2.models import Image

def slideshow(request):
    images = Image.objects.all()
    images_json = serializers.serialize('json', images)
    return render(request, 'part2/slideshow.html', {"images": images_json})
