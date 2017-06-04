from django.conf.urls import include, url
from django.contrib import admin

from django.contrib import admin
admin.autodiscover()

import oneverse_api

urlpatterns = [
    # Examples:
    # url(r'^$', 'oneverse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^oneverse-api/$', include(oneverse_api.urls)),
]
