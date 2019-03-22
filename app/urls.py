from django.urls import path 
from . import views

appname = 'app'

urlpatterns = [
	path("list/", views.StaffListView.as_view(), name="staff_list"),
	path("create/", views.StaffCreateView.as_view(), name="staff_create"),
	path("detail/<pk>", views.StaffDetailView.as_view(), name="staff_detail"),
	path("update/<pk>", views.StaffUpdateView.as_view(), name="staff_update"),
	path("delete/<pk>", views.StaffDeleteView.as_view(), name="staff_delete")
	# path("<int:id>/update/", views.StaffUpdateView.as_view(), name="staff_update")
]