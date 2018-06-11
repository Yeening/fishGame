from django.conf.urls import url,include
from django.contrib import admin
# from django.views.generic import redirect_to
from . import views

urlpatterns = [
    url(r'^$', views.game_view,name='game_view'),
    url(r'^(?P<user_id>[0-9]+)$', views.game_view,name='game_view'),
    # url(r'^id=(?:id-(?P<user_id>[0-9]+)/)?$', views.game_view,name='game_view'),

]