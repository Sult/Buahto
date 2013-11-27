from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	# url(r'^auth/$', views.auth_view, name='auth_view'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^register/$', views.register_user, name='register_user'),
	url(r'^register_success/$', views.register_success, name='register_success'),
)

