from django.conf.urls import patterns, include, url
from django.contrib import admin
import boleto.urls


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pyaboleto_templates_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^boleto/', include(boleto.urls)),
)
