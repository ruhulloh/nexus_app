from django.urls import path
from .views import main,login_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', main, name='main'),
    path('login/',login_view, name='login'),
    path('logout/',login_view, name='logout')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)