from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^addimg/$', views.add_img, name = 'addimg'),
    url(r'detail/', views.detail, name = 'detail'),
    url(r'^viewimg/(?P<year>\d{1,4})/(?P<month>\d{1,2})/$', views.viewimg, name = 'viewimg'),
    url(r'^login/$', views.user_login, name = 'login'),
    url(r'^logout/$', views.user_logout, name = 'logout'),
]
