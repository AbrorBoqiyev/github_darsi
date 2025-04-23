from django.urls import path
from .views import staff_form, staff_list, view_staff, update_staff, delete_staff


urlpatterns = [
    path("", staff_list, name="staff_list"),
    path("create", staff_form, name="create"),
    path('view/<int:pk>', view_staff, name="view-staff"),
    path("update/<int:pk>", update_staff, name="update-staff"),
    path("delete/<int:pk>", delete_staff, name="delete-staff"),
]


