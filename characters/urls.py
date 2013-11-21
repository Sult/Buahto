from django.conf.urls import patterns, url

from characters import views

urlpatterns = patterns('',
	url(r'^(?P<user_id>\d+)/characters/$', views.user_characters, name='user_characters'),
	url(r'^(?P<user_id>\d+)/create/$', views.create_character, name='create_character'),

)


	#url(r'^register/$', views.register_user, name='register_user'),
		#url(r'^(?P<character_id>\d+)/bounty/$', views.bounty, name='bounty'),


# ... your normal urlpatterns here

