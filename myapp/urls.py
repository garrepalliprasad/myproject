from django.urls import path
from . import views
urlpatterns=[
    path('show-departments',views.show_departments,name='show-departments'),
    path('create-department',views.create_department,name='create-department'),
    path('update-department/<int:pk>',views.update_department,name='update-department'),
    path('delete-department/<int:pk>',views.delete_department,name='delete-department'),
]