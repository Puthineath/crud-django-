from django.urls import path 
from . import views

appname = 'app'

urlpatterns = [
	path("list/", views.StaffListView.as_view(), name="staff_list"),
	path("create/", views.StaffCreateView.as_view(), name="staff_create"),
	path("<int:id>/detail/", views.StaffDetailView.as_view(), name="detail")
	# path("<int:id>/update/", views.StaffUpdateView.as_view(), name="staff_update")
]