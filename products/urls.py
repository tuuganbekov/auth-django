from django.urls import path
from products.views import ClassBasedView, RobotList, RobotDetail

urlpatterns = [
    path('info/', ClassBasedView.as_view()),
    path('products/', RobotList.as_view()),
    path('products/<int:pk>/', RobotDetail.as_view()),
]
