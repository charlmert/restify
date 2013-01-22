from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home$', 'rest.views.home', name='home'),
    url(r'^raw$', 'rest.views.raw', name='raw'),
    url(r'^morphy/(.*)$', 'rest.views.morphy', name='morphy'),
    url(r'^morphy/?P<word>(.*)$', 'rest.views.morphy', name='morphy'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
