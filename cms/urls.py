from django.contrib import admin
from django.urls import path
from documentmanage.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('signup/', signup),
    path('login/', signin),
    path('logout/', signout),
    path('sendrequest/', send_request),
    path('student/', student),
    path('manager/', manager),
    path('deleterequest/<int:reqid>/',deleterequest),
    path('adddocument/',adddocument),
    path('deletedocument/<int:deleteid>/',deletedocument),
    
]
