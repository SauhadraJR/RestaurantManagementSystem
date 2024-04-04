from django.urls import path
from .views import CustomUserViewSet

urlpatterns = [
    path('user/',CustomUserViewSet.as_view({'get':'list','post':'create'})),
    path('user/<int:pk>/',CustomUserViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
]