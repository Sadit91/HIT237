from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .pests_data import ITEMS, ip, f_d01  # Import our list of pest items
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def custom_404(request, exception):
    return render(request, "pests/404.html", status=404)

def home(request):
    # Retrieve the search term from GET parameters
    query = request.GET.get('q', '')
    
    # Only filter if a search term is provided; otherwise, return an empty list.
    if query:
        filtered_items = [
            item for item in ITEMS 
            if query.lower() in item.name.lower() or query.lower() in item.brief_description.lower()
        ]
    else:
        filtered_items = []  # Show no items if no search term is provided

    ctx = {
        'items': filtered_items,
        'query': query,
    }
    return render(request, 'pests/home.html', ctx)

# Project List View (ListView)

class pro_list(ListView):
    template_name = "pests/proj_list.html"
    context_object_name = "itms"

    def get_queryset(self):
        ftype = self.request.GET.get("type", "")
        if ftype == "pest":
            return [i for i in ITEMS if isinstance(i, ip)]
        elif ftype == "disease":
            return [i for i in ITEMS if isinstance(i, f_d01)]
        return ITEMS

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["ftype"] = self.request.GET.get("type", "")
        return ctx

# DetailView for each pest/disease item
class pro_det(DetailView):
    template_name = "pests/project_detail.html"
    context_object_name = "itm"

    def get_object(self):
        pid = self.kwargs.get("pid")
        pid = self.kwargs.get("pid")
        itm = next((i for i in ITEMS if str(i.id) == str(pid)), None)
        if not itm:
            raise Http404("Item not found")
        return itm


def about(request):
    tm = [
        {'n': 'Sadit Khan.', 'student_id': 'S379452'},
        {'n': 'Nguyen Hao Vo.', 'student_id': 'S377196'},
        {'n': 'Fabiha Sultana Anushe.', 'student_id': 'S372205'},
        {'n': 'Roshan Karki.', 'student_id': 'S365632'},
    ]
    ctx = {'tm': tm}
    return render(request, 'pests/about.html', ctx)