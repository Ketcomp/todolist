from django.conf.urls import url, patterns
from . import views

urlpatterns = [
        url(r'^items/$', views.ToDoItemList.as_view()),
        url(r'^items/(?P<pk>[0-9]+)/$', views.ToDoItem.as_view()),
        url(r'^lists/$', views.ToDoLists.as_view()),
        url(r'^lists/(?P<pk>[0-9]+)/$', views.ToDoList.as_view())
        #url(r'^$', views.index, name='home'),
        #url(r'^dbtest$', views.db_test, name='dbtest'),
]
