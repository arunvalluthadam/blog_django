from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_projects.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    # blog app base url
    (r'^blogs/', include('blog.urls')),
    
    # paint app base url
    #(r'^paint_app/', include('paint_app.urls')),
)
