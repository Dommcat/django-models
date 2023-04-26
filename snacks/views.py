from django.views.generic import ListView, DetailView
from .models import Snack

# Create your views here.
class SnacksListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack
    context_object_name = 'snacks_tracking_project'


class SnacksDetailView(DetailView):
    template_name = 'snacks_detail.html'
    model = Snack
    context_object_name = 'detail_snacks_tracking_project'

    




# class AboutPageView(TemplateView):
#     template_name = 'about.html'