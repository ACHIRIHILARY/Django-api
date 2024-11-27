from django.urls import path
from . import views

urlpatterns = [
    path('Blockpost/', views.BlockPostListCreate.as_view(), name="blockpost_view_create"),
    path('Blockpost/<int:pk>', views.BlockpostRetrieveUpdateDestroy.as_view(), name="update")
]
    