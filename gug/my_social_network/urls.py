from django.conf.urls import patterns, url, include
import views 

urlpatterns = patterns('', 
                       url(r'^users/$', views.users_list, name='users_list'), 
                       url(r'^(?P<user_id>\w+)/followers/$', views.users_followers, name='users_followers'),
                       url(r'^(?P<user_id>\w+)/following/$', views.users_following, name='users_following'),
)  