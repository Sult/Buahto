from django.conf.urls import patterns, url

from characters import views

urlpatterns = patterns('',
	url(r'^characters/$', views.characters, name='characters'),
	url(r'^create/$', views.create_character, name='create_character'),
	url(r'^profile/(?P<character_name>[^/]+)/$', views.profile, name='profile'),
	url(r'^login/(?P<character_name>[^/]+)$', views.login_character, name='login_character'),
	
	#ingame character views
	url(r'^remap/$', views.remap, name='remap'),
)
