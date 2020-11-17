from django.conf.urls import include
from django.urls import path

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView

from filebrowser.sites import site as filebrowser_sites

from django.contrib.admin import site
import adminactions.actions as actions


actions.add_to_site(site)


class RobotsView(TemplateView):
    template_name = "robots.txt"


urlpatterns = [
    path(r'', include('rotv_apps.urls')),

    # maintain
    path(r'robots.txt', RobotsView.as_view(), name='robots'),

    # administration
    path('admin/filebrowser/', filebrowser_sites.urls),
    path('grappelli/', include('grappelli.urls')),
    path('adminactions/', include('adminactions.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
