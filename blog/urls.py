from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from blog.views import likeView, post_add,blog_update,blog_delete,blog_detail




urlpatterns = [
    path('new_post/',post_add,name='new_post'),
    path('update/<slug:slug>', blog_update, name='update'),
    path('delete/<slug:slug>', blog_delete, name='delete'),
    path("detail/<slug:slug>", blog_detail, name="detail"),
    path('post_like/<int:pk>', likeView, name="post_like"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
    
