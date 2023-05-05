#from django.urls import path, include
#from rest_framework import routers
#from .views import PostViewSet

#router = routers.DefaultRouter()

##router.register(r'posts', PostViewSet)

#urlpatterns = [
 #   path('', include(router.urls)),
 #   path('api/', include('rest_framework.urls', namespace='rest_framework'))
#]

from django.urls import path
from ratings import views

urlpatterns = [
    path('rating/<int:post_id>/<int:rating>/', views.rating),
    path('ratings/', views.index),
]