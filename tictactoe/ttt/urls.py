from django.conf.urls.defaults import *
from tictactoe.ttt import views

urlpatterns= patterns ('',
    url(r'^$', views.index, name='index'),
    url(r'^start_game/$', views.startGame, name='start_game'),
    url(r'^save_x/(?P<boardId>\d+)/(?P<row>\d+)/(?P<col>\d+)/$', views.saveUserX, name='save_x'),
#    url(r'^start_o/(?P<boardId>\d+)/(?P<row>\d+)/(?P<col>\d+)/$', views.saveUserO, name='save_o'),
)
