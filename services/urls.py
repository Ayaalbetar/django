from django.urls import path

from services import views

urlpatterns = [
    path('', views.index, name='iindex'),
    path('services', views.services,name='sservices'),
    path('about',views.about,name='about'),
    path('projects',views.projects,name='projects'),
    #path('services/student',views.student, name='student')
    #notifications
    path('notifs',views.notifs,name='notifs'),
    path('get_notifs',views.get_notifs,name='get_notifs'),
    path('getnotif', views.getnotif, name='getnotif'),
    path('nn', views.nn, name='nn'),
    path('mark_read_notif',views.mark_read_notif,name='mark_read_notif'),
]