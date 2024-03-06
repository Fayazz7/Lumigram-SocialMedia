"""
URL configuration for lumigram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserAuthView.as_view(), name="authentication"),
    path('logout', views.SignOutView.as_view(), name="sign-out"),
    path("home", views.IndexView.as_view(), name="home"),
    path('post/create', views.CreatePostView.as_view(), name='new-post'),
    path('profile/<int:pk>/retrieve',views.ProfileView.as_view(),name='profile-view'),
    path('profile/<int:pk>/update',views.ProfileUpdateView.as_view(),name='profile-update'),
    path('connect/<int:pk>',views.FollowUnFollowView.as_view(),name='connect')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
