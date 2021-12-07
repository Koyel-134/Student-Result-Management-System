from . import views
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("login/",views.login),
    path("logout/",views.logout),
    path("about/",views.about),
    path("result/",views.result),
    path("logined/",views.logined),
    path("registered/",views.registered),
    path("",views.home),
    path("contact/",views.contact),
    path("forgetpass2/",views.forgetpass2),
    path("editpassword/",views.editpassword),
    path("editpassword2/",views.editpassword2),
    path("forget/",views.forget),
    path("forget2/",views.forget2),
    path("deleted/",views.deleted),
    path("add/",views.add),
    path("delete/",views.delete),
    path("update/",views.update),
    path("updated/",views.updated),
    path("show/",views.show),
    path("add2/",views.add2),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
