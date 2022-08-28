from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from site_core import views
from site_core.views import HomeView, PhotoCreateView, PhotoListView, \
    SignUpView, ContactView, PhotoDeleteView

app_name = 'site_core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_photo/', PhotoCreateView.as_view(), name = 'create_photo'),
    path('list_photo/', PhotoListView.as_view(), name = 'list_photo'),
    path('signup/', SignUpView.as_view(), name = 'signup'),
    path('contact_form/', ContactView.as_view(), name = 'contact_form'),
    path('gallery/', views.gallery, name='gallery'),
    path('email_success/', views.email_success, name = 'email_success'),
    path('photo_delete/<int:pk>', PhotoDeleteView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'site_core.views.view_404'