from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('login/', views.signin, name="login"),
    path('postsign/', views.postsign),
    path("postsign/logout/", LogoutView.as_view(), name="logout"),
    path('register/', views.register, name="register"),
    path("postregister/", views.postregister, name="postregister"),
]
