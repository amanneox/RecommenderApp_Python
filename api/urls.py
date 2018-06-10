from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
from api.views import CustomAuthToken
urlpatterns = [
    url(r'^posts/$', views.post_list),
    url(r'^posts/(?P<pk>[0-9a-f]+)$', views.post_detail),
    url(r'^users/$', views.user_list),
    url(r'^users/(?P<pk>[0-9a-f]+)$', views.user_detail),
    url(r'^services/$', views.service_list),
    url(r'^services/(?P<pk>[0-9a-f]+)$', views.service_detail),
    url(r'^items/$', views.item_list),
    url(r'^items/(?P<pk>[0-9a-f]+)$', views.item_detail),
    url(r'^item/comments/$',views.comment_list),
    url(r'^items/loc/$', views.location_item_list),
    url(r'^token/', CustomAuthToken.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)