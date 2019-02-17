from django.shortcuts import render
from .models import Wpis
from django.utils import timezone

# Create your views here.

def post_list(request):
    posts=Wpis.objects.filter(data_publikacji__lte=timezone.now()).order_by('data_publikacji')
    return render(request, 'blog/post_list.html', {'posts': posts})