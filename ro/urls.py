from django.conf.urls import url, include

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
    url(r'', include('rotv_apps.urls')),

    # maintain
    url(r'^robots.txt$', RobotsView.as_view(), name='robots'),

    # administration
    url(r'^admin/filebrowser/', include(filebrowser_sites.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^adminactions/', include('adminactions.urls')),
    url(r'^admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
