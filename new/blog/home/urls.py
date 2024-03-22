from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


app_name = 'home'

urlpatterns = [
    #path('', views.PostList.as_view(), name='home'),
    path('', views.home, name='home'),
    #single page
    path('detail/<slug>', views.detail, name="detail"),
     #new post
    path('new-post/', views.new_post, name="new_post"),
     #edit post
    path('edit/<post_id>', views.edit_post, name="edit_post"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)