from django.urls import path
from user import views
from django.conf.urls import url
urlpatterns = [
    # 将函数绑定至对应路由
    url('', views.main_page),

    url('add/$',views.add_note),

    url('del/',views.del_note),

    url('modify/',views.modify_note),

    url('change/',views.change_note_status)


]
