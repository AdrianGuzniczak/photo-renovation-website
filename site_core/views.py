from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from site_core.models import Contact, Photo
from . forms import ContactForm, SignupForm


class HomeView(TemplateView):
    template_name = 'site_core/home.html'

class PhotoCreateView(LoginRequiredMixin, CreateView):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    model = Photo
    fields = ['description', 'photo']
    success_url = reverse_lazy('site_core:list_photo')

class PhotoListView(LoginRequiredMixin, ListView):
    model = Photo
    context_object_name = 'photo_list'
    template_name = 'site_core/photo_list.html'

    def get_queryset(self):
        '''This method displays photos that belong to the currently logged in user.'''

        return Photo.objects.filter(owner=self.request.user)

class SignUpView(generic.CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'site_core/contact_form.html'
    success_url = reverse_lazy('site_core:home')

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form)

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = reverse_lazy('site_core:list_photo')

def gallery(request):
    return render(request,"site_core/gallery.html")

def email_success(request):
    return render(request, "site_core/email_success.html")

def view_404(request, exception=None):
    return redirect('site_core/home')