from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from site_core.models import Contact, Photo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.conf import settings
from . forms import ContactForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'site_core/home.html'

class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['renovation', 'coloring', 'description', 'photo']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('site_core:list_photo')

class PhotoListView(LoginRequiredMixin, ListView):
    model = Photo
    context_object_name = 'photo_list'
    template_name = 'site_core/photo_list.html'

    def get_queryset(self):
        return Photo.objects.filter(owner=self.request.user)
        

class PhotoDetailView(DetailView):
    model = Photo

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ContactView(CreateView):
    
    model = Contact
    # model = Contact
    form_class = ContactForm
    template_name = 'site_core/contact_form.html'

def gallery(request):
     return render(request,"site_core/gallery.html")
    

