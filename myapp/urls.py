from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('show-departments',views.show_departments,name='show-departments'),
    path('create-department',views.create_department,name='create-department'),
    path('update-department/<int:id>',views.update_department,name='update-department'),
    path('delete-department/<int:id>',views.delete_department,name='delete-department'),
    path('show-faculties',views.show_faculties,name='show-faculties'),
    path('create-faculty',views.create_faculty,name='create-faculty'),
    path('update-faculty/<int:id>',views.update_faculty,name='update-faculty'),
    path('delete-faculty/<int:id>',views.delete_faculty,name='delete-faculty'),
]