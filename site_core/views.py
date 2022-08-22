from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from site_core.models import Photo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.
class HomeView(TemplateView):
    template_name = 'site_core/home.html'

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = '__all__'
    success_url = reverse_lazy('site_core:list_photo')

class PhotoListView(LoginRequiredMixin, ListView):
    model = Photo
    context_object_name = 'photo_list'
    paginate_by = 5

    def get_queryset(self):
        print('>>>>>>>>>>>>>>>>>>{}'.format(self.request.user))
        return Photo.objects.filter(user = self.request.user)

class PhotoDetailView(DetailView):
    model = Photo

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


