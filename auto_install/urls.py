from django.conf.urls import patterns, include, url
from django.contrib import admin
from pxe.views import *
from django.views.generic.base import RedirectView
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auto_install.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^start/(\d+)',start),
    url(r'^online/(?P<obj_id>\d+)',online_view),
    url(r'^edit/(?P<obj_id>\d+)',edit),
    url(r'^info/(\d+)', info, name='info'),
    url(r'^exe/',exe_page,name="exe"),
    url(r'^$', login_view,name='login'),
    url(r'^find/',find_page,name='find'),
    url(r'^logout/', logout_page, name="logout"),
    url(r'^del/(\d+)',del_obj),
    url(r'^lock/(?P<obj_id>\d+)/(?P<obj_code>True|False)',lock_obj),
    url(r'^ing/(?P<o_id>\d+)',ing),
    url(r'^post/',register_post),
    url(r'^his/',his_page,name="his"),
    url(r'^finish/',finish_api),
    url(r'^admin/', include(admin.site.urls)),
)