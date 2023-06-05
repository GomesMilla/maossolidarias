from django.contrib import admin
from django.urls import path
from django.urls import path, include, re_path
from ckeditor_uploader import views as ckeditor_view
from django.conf.urls.static import static
from ckeditor_uploader import views as ckeditor_views
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.static import serve
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), 
    path('base/', include('base.urls')), 
    path("", TemplateView.as_view(template_name="presentation/objetivo.html"), name="objetivo"),
    path('ckeditor/upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)), name='ckeditor_browse'),


    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
