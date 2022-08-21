from django.urls import path
from site_core.views import HomeView, PhotoCreateView, ThankYouView, PhotoListView

app_name = 'site_core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_photo/', PhotoCreateView.as_view(), name = 'create_photo'),
    path('thank_you/', ThankYouView.as_view(), name='thank_you'),
    path('list_photo/', PhotoListView.as_view(), name = 'list_photo'),
]