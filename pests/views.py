# pests/views.py

from django.shortcuts import render
from .pests_data import itms  # Import our list of pest items

def home(request):
    return render(request, 'pests/home.html')

# Renamed function to match the URL config
def proj_list(request):
    ctx = {'itms': itms}
    return render(request, 'pests/project_list.html', ctx)

def proj_det(request, pid):
    itm = next((p for p in itms if str(p.id) == str(pid)), None)
    if not itm:
        return render(request, 'pests/404.html', status=404)
    ctx = {'itm': itm}
    return render(request, 'pests/project_detail.html', ctx)

def about(request):
    tm = [
        {'n': 'Sadit Khan.', 'id': 'S379452'},
        {'n': 'Nguyen Hao Vo.', 'id': 'S377196'},
        {'n': 'Fabiha Sultana Anushe.', 'id': 'S372205'},
        {'n': 'Roshan Karki.', 'id': 'S365632'},
    ]
    ctx = {'tm': tm}
    return render(request, 'pests/about.html', ctx)
