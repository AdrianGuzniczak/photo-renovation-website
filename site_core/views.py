from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from site_core.models import Photo

# Create your views here.
class HomeView(TemplateView):
    template_name = 'site_core/home.html'

class ThankYouView(TemplateView):
    template_name = 'site_core/thank_you.html'

class PhotoCreateView(CreateView):
    model = Photo
    fields = "__all__"
    success_url = reverse_lazy('site_core:thank_you')

class PhotoListView(ListView):
    model = Photo
    context_object_name = 'photo_list'