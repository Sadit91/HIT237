from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .pests_data import ITEMS  # Import our list of pest items
from django.http import Http404

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
    template_name = "pests/proj_list.html"  # Template to use
    context_object_name = "itms"  # Name of the context variable to use in the template

    def get_queryset(self):
        """Return the list of pest/disease items."""
        return ITEMS  # Return the global ITEMS list

# Project Detail View (DetailView)

class pro_det(DetailView):
    template_name = "pests/project_detail.html"  # Same shit as above for Project Detail
    context_object_name = "itm" 

    def get_object(self):
        """Retrieve the project item by 'pid'."""
        pid = self.kwargs.get("pid")  # Capture 'pid' from URL
        # If there's a slug (e.g., '123-item-name'), just take the numeric part
        pid = str(pid).split("-")[0]  # Extract numeric part from pid string
        # Search for the item in the global ITEMS list
        itm = next((p for p in ITEMS if str(p.id) == pid), None)
        if itm is None:
            raise Http404(f"No project found with id {pid}")  # Return 404 if not found
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