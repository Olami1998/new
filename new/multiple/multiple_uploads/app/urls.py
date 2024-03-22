from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('up', views.upload, name='uploadView'),
    path('', views.load, name='upView'),
    #path('delete', views.deleteProduct, name='delete-prod'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)