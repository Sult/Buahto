from django.conf.urls import patterns, url

from towns import views

urlpatterns = patterns('',
	url(r'^training/$', views.training, name='training'),
	url(r'^trainingground/$', views.trainingground, name='trainingground'),

)
