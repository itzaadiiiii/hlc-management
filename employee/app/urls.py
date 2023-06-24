from django.urls import path
from .views import *


urlpatterns = [
    path('a1/',adddepartment, name='adddept'),
    path('sd/',showdepartment,name='showdept'),
    path('ud/<int:id>/',updatedepartment,name='updatedept'),
    path('dd/<int:id>/',deletedepartment,name='deletedept'),
    path('',addemployee,name='addemp'),
    path('se/',showemployee,name='showemp'),
    path('ue/<int:id>/',updateemployee,name='updateemp'),
    path('de/<int:id>/',deleteemployee,name='deleteemp'),
    path('fe/',filter,name='searchemp'),
]
