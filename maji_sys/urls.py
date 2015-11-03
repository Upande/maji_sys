from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from .views import IndexView, DataForm
from .views import *

urlpatterns = patterns('',
	#url(r'^$', IndexView.as_view(), name='index'),
	url(r'^$', DataForm.as_view(), name='index'),
	url(r'^DataForm/$', DataForm.as_view(), name='data_form'),
	url(r'^submit/$',  submit, name='submit'),
	#url(r'^data-form/$', submit, name='submit'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login',
		{'template_name': 'login.html'}, name='auth_login'),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='auth_logout'),
	#url(r'^.*$', RedirectView.as_view(url='DataForm', permanent=False), name='default'),
	(r'^feature/(?P<feature>[-\w]+)/all_json_models/$', all_json_models),
)
