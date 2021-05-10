
from django.contrib import admin
from django.urls import path , include  #to include app.urls and other files

#main project urls file 
admin.site.site_header = "SAKSHAM! Admin"
admin.site.site_title = "SAKSHAM Admin Portal"
admin.site.index_title = "Welcome to SAKSAM"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))   
]
