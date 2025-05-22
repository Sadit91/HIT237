from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Pest, Disease
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import FarmForm, SurveillanceSessionForm, ObservationForm
from .models import Farm, SurveillanceSession, Observation
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from .models import Grower
from django.utils.timezone import now, timedelta
from django.db.models import Count
import json
from math import ceil
from .forms import SurveillanceEffortForm

def custom_404(request, exception):
    return render(request, "pests/404.html", status=404)

def home(request):
    query = request.GET.get('q', '')
    items = []

    if query:
        pest_results = Pest.objects.filter(name__icontains=query) | Pest.objects.filter(brief_description__icontains=query)
        disease_results = Disease.objects.filter(name__icontains=query) | Disease.objects.filter(brief_description__icontains=query)
        items = list(pest_results) + list(disease_results)

    ctx = {
        'items': items,
        'query': query,
    }
    return render(request, 'pests/home.html', ctx)

class pro_list(ListView):
    template_name = "pests/proj_list.html"
    context_object_name = "itms"

    def get_queryset(self):
        ftype = self.request.GET.get("type", "")
        if ftype == "pest":
            return Pest.objects.all()
        elif ftype == "disease":
            return Disease.objects.all()
        return list(Pest.objects.all()) + list(Disease.objects.all())

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["ftype"] = self.request.GET.get("type", "")
        return ctx

class pro_det(DetailView):
    template_name = "pests/project_detail.html"
    context_object_name = "itm"

    def get_object(self):
        pid = self.kwargs.get("pid")
        itype = self.kwargs.get("itype")
        if itype == "pest":
            return get_object_or_404(Pest, id=pid)
        elif itype == "disease":
            return get_object_or_404(Disease, id=pid)
        raise Http404("Invalid type")

def about(request):
    tm = [
        {'n': 'Sadit Khan.', 'student_id': 'S379452'},
        {'n': 'Nguyen Hao Vo.', 'student_id': 'S377196'},
        {'n': 'Fabiha Sultana Anushe.', 'student_id': 'S372205'},
        {'n': 'Roshan Karki.', 'student_id': 'S365632'},
    ]
    ctx = {'tm': tm}
    return render(request, 'pests/about.html', ctx)

# -------- FARM VIEWS --------
class FarmListView(ListView):
    model = Farm
    template_name = 'pests/portal/farm_list.html'
    context_object_name = 'farms'

    def get_queryset(self):
        return Farm.objects.filter(grower=self.request.user.grower)

class FarmCreateView(CreateView):
    model = Farm
    form_class = FarmForm
    template_name = 'pests/portal/farm_form.html'
    success_url = reverse_lazy('farm_list')

    def form_valid(self, form):
        form.instance.grower = self.request.user.grower
        return super().form_valid(form)

class FarmUpdateView(UpdateView):
    model = Farm
    form_class = FarmForm
    template_name = 'pests/portal/farm_form.html'
    success_url = reverse_lazy('farm_list')

class FarmDeleteView(DeleteView):
    model = Farm
    template_name = 'pests/portal/farm_confirm_delete.html'
    success_url = reverse_lazy('farm_list')

# -------- SESSION VIEWS --------
class SessionListView(ListView):
    model = SurveillanceSession
    template_name = 'pests/portal/session_list.html'
    context_object_name = 'sessions'

    def get_queryset(self):
        return SurveillanceSession.objects.filter(farm__grower=self.request.user.grower)

class SessionCreateView(CreateView):
    model = SurveillanceSession
    form_class = SurveillanceSessionForm
    template_name = 'pests/portal/session_form.html'
    success_url = reverse_lazy('session_list')

    def form_valid(self, form):
        # Try to assign the first available farm for the current grower
        farms = Farm.objects.filter(grower=self.request.user.grower)
        if farms.exists():
            form.instance.farm = farms.first()
        else:
            form.add_error(None, "You must have a farm before creating a session.")
            return self.form_invalid(form)
        return super().form_valid(form)

class SessionUpdateView(UpdateView):
    model = SurveillanceSession
    form_class = SurveillanceSessionForm
    template_name = 'pests/portal/session_form.html'
    success_url = reverse_lazy('session_list')

class SessionDeleteView(DeleteView):
    model = SurveillanceSession
    template_name = 'pests/portal/session_confirm_delete.html'
    success_url = reverse_lazy('session_list')

# -------- OBSERVATION VIEWS --------
class ObservationListView(ListView):
    model = Observation
    template_name = 'pests/portal/observation_list.html'
    context_object_name = 'observations'

    def get_queryset(self):
        return Observation.objects.filter(session__farm__grower=self.request.user.grower)

class ObservationCreateView(CreateView):
    model = Observation
    form_class = ObservationForm
    template_name = 'pests/portal/observation_form.html'
    success_url = reverse_lazy('observation_list')

    def form_valid(self, form):
        sessions = SurveillanceSession.objects.filter(farm__grower=self.request.user.grower)
        if sessions.exists():
            form.instance.session = sessions.first()
            return super().form_valid(form)
        else:
            form.add_error(None, "No available surveillance sessions. Please create one first.")
            return self.form_invalid(form)

class ObservationUpdateView(UpdateView):
    model = Observation
    form_class = ObservationForm
    template_name = 'pests/portal/observation_form.html'
    success_url = reverse_lazy('observation_list')

class ObservationDeleteView(DeleteView):
    model = Observation
    template_name = 'pests/portal/observation_confirm_delete.html'
    success_url = reverse_lazy('observation_list')

@login_required
def grower_portal(request):
    grower = request.user.grower
    today = now().date()
    past_30_days = today - timedelta(days=30)

    farm_count = Farm.objects.filter(grower=grower).count()
    session_count = SurveillanceSession.objects.filter(farm__grower=grower).count()
    observation_count = Observation.objects.filter(session__farm__grower=grower).count()

    # New: Filtered by date
    recent_sessions = SurveillanceSession.objects.filter(
        farm__grower=grower,
        date__gte=past_30_days
    ).count()

    recent_observations = Observation.objects.filter(
        session__farm__grower=grower,
        session__date__gte=past_30_days
    ).count()

    return render(request, "pests/portal.html", {
        "farm_count": farm_count,
        "session_count": session_count,
        "observation_count": observation_count,
        "recent_sessions": recent_sessions,
        "recent_observations": recent_observations
    })


# -------- REGISTRATION VIEW --------
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Auto-create linked Grower profile
            Grower.objects.create(user=user, name=user.username, age=0, email=user.email)
            login(request, user)
            return redirect('grower_portal')
    else:
        form = UserCreationForm()
    return render(request, 'pests/registration/register.html', {'form': form})

# -------- LOGOUT VIEW --------
def logout_view(request):
    logout(request)
    return redirect('home')

# -------- DASHBOARD --------
@login_required
def grower_portal(request):
    grower = request.user.grower
    today = now().date()
    past_30_days = today - timedelta(days=30)

    # Summary counts
    farm_count = Farm.objects.filter(grower=grower).count()
    session_count = SurveillanceSession.objects.filter(farm__grower=grower).count()
    observation_count = Observation.objects.filter(session__farm__grower=grower).count()

    # Recent 30-day counts
    recent_sessions = SurveillanceSession.objects.filter(
        farm__grower=grower,
        date__gte=past_30_days
    ).count()

    recent_observations = Observation.objects.filter(
        session__farm__grower=grower,
        session__date__gte=past_30_days
    ).count()

    # Sessions by plant type (for chart)
    session_data = SurveillanceSession.objects.filter(farm__grower=grower).values(
        'plant_type__name'
    ).annotate(count=Count('id'))

    plant_labels = [item['plant_type__name'] for item in session_data]
    plant_counts = [item['count'] for item in session_data]

    return render(request, "pests/portal.html", {
        "farm_count": farm_count,
        "session_count": session_count,
        "observation_count": observation_count,
        "recent_sessions": recent_sessions,
        "recent_observations": recent_observations,
        "plant_labels": json.dumps(plant_labels),
        "plant_counts": json.dumps(plant_counts)
    })

# -------- SURVEILLANCE EFFORT FORM --------

def effort_calculator(request):
    result = None
    plant_count = season = plant_part = None

    if request.method == "POST":
        form = SurveillanceEffortForm(request.POST)
        if form.is_valid():
            plant_count = form.cleaned_data["plant_count"]
            season = form.cleaned_data["season"]
            plant_part = form.cleaned_data["plant_part"]

            # Basic multiplier logic
            multiplier = 1.5 if season == "wet" else 1.0
            result = ceil((plant_count ** 0.5) * multiplier)
    else:
        form = SurveillanceEffortForm()

    return render(request, "pests/portal/effort_calculator.html", {
        "form": form,
        "result": result,
        "plant_count": plant_count,
        "season": season,
        "plant_part": plant_part,
    })
