from django.conf.urls.defaults import *

urlpatterns = patterns('djangoajaxtest.basic',
    # Example:
    (r'^$', 'views.index'),
    (r'^ajax/store_message$', 'ajax.store_message'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
