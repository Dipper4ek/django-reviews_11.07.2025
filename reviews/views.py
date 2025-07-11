from django.shortcuts import render
from .models import Review

def index(request):
    reviews = Review.objects.all().order_by('-date')
    return render(request, 'reviews/index.html', {'reviews': reviews})
