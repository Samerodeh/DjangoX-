from .models import Snack
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

# Create your views here.

class SnackListView(ListView):
    template_name = 'snacks/snack_list.html'
    model = Snack

class SnackDetailsView(DetailView):
    template_name = 'snacks/snack_details.html'
    model = Snack


class SnackCreateView(CreateView):
    template_name = 'snacks/snack_create.html'
    model = Snack
    fields=['title' ,'purchaser','description']


class SnackUpdateView(UpdateView):
    template_name = 'snacks/snack_update.html'
    model = Snack
    fields=['title' ,'purchaser','description']


class SnackDeleteView(DeleteView):
    template_name = 'snacks/snack_delete.html'
    model = Snack
    success_url=reverse_lazy('snack_list')
