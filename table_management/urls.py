from django.urls import path
from .views import TableViewSet

urlpatterns = [
    path('user/',TableViewSet.as_view({'get':'list','post':'create'})),
    path('user/<int:pk>/',TableViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
]