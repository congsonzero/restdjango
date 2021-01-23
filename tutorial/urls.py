from django.conf.urls import url 
from tutorial import views 
 
urlpatterns = [ 
    url(r'^api/tutorial$', views.tutorial_list),
    url(r'^api/tutorial/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^api/tutorial/published$', views.tutorial_list_published),
    url(r'^hello', views.hello),
]