from django.shortcuts import render

import viewer

def index(request):
    return render(request, 'index.html')