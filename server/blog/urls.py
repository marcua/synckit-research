from django.conf.urls.defaults import *


urlpatterns = patterns('emailstubs',
    # Example:
    # (r'^server/', include('server.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^inbox$', 'emailqueue.inbox'),
)
