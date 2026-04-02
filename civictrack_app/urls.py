from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('comment/<int:report_id>/', views.add_comment),  # 👈 THIS
]