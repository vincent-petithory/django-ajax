from django.conf.urls.defaults import *

import os

urlpatterns = patterns('',
    # Example:
    (r'^basic/', include('djangoajaxtest.basic.urls')),
    (r'^basicmedia/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '%s/basic/media' % os.getcwd()}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
