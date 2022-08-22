from django.urls import path
from site_core.views import HomeView, PhotoCreateView, PhotoListView, PhotoDetailView, SignUpView

app_name = 'site_core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create_photo/', PhotoCreateView.as_view(), name = 'create_photo'),
    path('list_photo/', PhotoListView.as_view(), name = 'list_photo'),
    path('photo_detail/<int:pk>', PhotoDetailView.as_view(), name = 'detail_photo'),
    path('signup/', SignUpView.as_view(), name = 'signup')
]