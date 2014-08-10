from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'opos.views.dashboard', name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
