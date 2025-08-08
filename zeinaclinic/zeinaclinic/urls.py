from django.contrib import admin
from django.urls import path
from patient import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),            # 👈 shows patient list
    path('add/', views.add_patient, name='add_patient'),
    path('edit/<int:pk>/', views.edit_patient, name='edit_patient'),
    path('delete/<int:pk>/', views.delete_patient, name='delete_patient'),

  
]
