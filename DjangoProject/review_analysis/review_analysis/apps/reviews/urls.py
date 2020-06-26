from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('leave_review/', views.leave_review, name = 'leave_review')
]