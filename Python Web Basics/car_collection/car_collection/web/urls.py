from django.urls import path

from car_collection.web.views import show_index, create_profile, show_catalogue, create_car, details_car, edit_car, \
    delete_car, details_profile, edit_profile, delete_profile

urlpatterns = (
    path("", show_index, name="show index"),
    path("profile/create", create_profile, name="create profile"),
    path("catalogue/", show_catalogue, name="show catalogue"),
    path("car/create/", create_car, name="create car"),
    path("car/<int:id>/details/", details_car, name="details car"),
    path("car/<int:id>/edit/", edit_car, name="edit car"),
    path("car/<int:id>/delete/", delete_car, name="delete car"),
    path("profile/details/", details_profile, name="details profile"),
    path("profile/edit/", edit_profile, name="edit profile"),
    path("profile/delete/", delete_profile, name="delete profile"),

)
