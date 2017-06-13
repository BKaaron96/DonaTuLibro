from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import login
app_name='dona'
urlpatterns = [

    url(r'^inicio/$', views.inicio, name='inicio'),
    url(r'^login/$', views.login, name='login'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^registro/registroexitoso/$', views.registroexitoso, name='registroexitoso'),
    url(r'^logout/$', views.logoutp, name='logoutp'),

]
