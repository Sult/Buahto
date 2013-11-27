from django.conf.urls import patterns, url

from characters import views

urlpatterns = patterns('',
	url(r'^characters/$', views.characters, name='characters'),
	url(r'^create/$', views.create_character, name='create_character'),
	url(r'^profile/(?P<character_name>[^/]+)/$', views.character_profile, name='character_profile'),
	url(r'^login/(?P<character_name>[^/]+)$', views.login_character, name='login_character'),
)
