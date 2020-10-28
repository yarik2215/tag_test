from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tags',views.TagViewSet)
# router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/user_tags/', views.UserTagsView.as_view()),
    path('api/user_list/', views.UserListView.as_view()),
    
]
