from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crepes_bretonnes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accueil/$', 'blog.views.home'),
    url(r'^blog/', include('blog.urls')),
    
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
