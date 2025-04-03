# pests/views.py

from django.shortcuts import render
from .pests_data import ITEMS  # Import our list of pest items

def home(request):
    return render(request, 'pests/home.html')

# Renamed function to match the URL config
def proj_list(request):
    # Pass the list of items to the template context.
    context = {'itms': ITEMS}
    return render(request, 'pests/proj_list.html', context)


def proj_det(request, pid):
    itm = next((p for p in ITEMS if str(p.id) == str(pid)), None)
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


