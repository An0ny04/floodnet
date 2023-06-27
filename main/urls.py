from django.urls import path
from .views import dashboard,dashboard_login,dashboard_logout,image_upload,list_images,dashboard_register


urlpatterns = [
    path("", dashboard,name="home"),
    path("login", dashboard_login,name="login"),
    path("register", dashboard_register,name="register"),
    path("logout", dashboard_logout,name="logout"),
    path("upload", image_upload,name="imageupload"),
    path("listimages", list_images,name="listimages"),

]
