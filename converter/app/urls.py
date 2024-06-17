from . import views
import os
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, SongView

API_PREFIX = "api/"

urlpatterns = [
    path('', HomeView.as_view()),
    path(API_PREFIX + 'song/', SongView.as_view()),
]

urlpatterns += static('tmp/', document_root=os.path.join(settings.BASE_DIR, 'tmp/'))