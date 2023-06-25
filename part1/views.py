from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone

def index(request):
    # Get the number of visits from the cookie
    visits = int(request.COOKIES.get('visits', '0'))
    visits += 1

    # Set the cookie with the updated visit count
    response = HttpResponse(render(request, 'part1/cookie.html', {'visits': visits}))
    response.set_cookie('visits', str(visits), expires=timezone.now() + timezone.timedelta(days=365))

    return response
