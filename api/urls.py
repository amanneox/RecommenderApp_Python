from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^posts/$', views.post_list),
    url(r'^posts/(?P<pk>[0-9a-f]+)$', views.post_detail),
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9a-f]+)$', views.user_detail),
    url(r'^services/$', views.service_list),
    url(r'^services/(?P<pk>[0-9a-f]+)$', views.item_list),
    url(r'^items/$', views.service_list),
    url(r'^items/(?P<pk>[0-9a-f]+)$', views.item_detail),


]

urlpatterns = format_suffix_patterns(urlpatterns)