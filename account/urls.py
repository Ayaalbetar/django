from django.urls import path
from . import views
urlpatterns=[
    path('1' ,views.student, name='student'),
    path('2',views.orphan, name='orphan'),
    path('3',views.family, name='family'),
    path('4', views.medican, name='medican'),
    path('5',views.patient,name='patient'),
    path('all',views.allhos,name='allhos'),
    path('basket',views.basket,name='basket'),
    path('all/albir/eye',views.albir_eye,name='albir_eye')
]
