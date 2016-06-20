from django.conf.urls import url, patterns
from . import views

urlpatterns = [
        url(r'^$', views.index, name='home'),
        url(r'^dbtest$', views.db_test, name='dbtest'),
]
