from django.urls import path
from dashboard.views import user_homepage

urlpatterns = [
    path("Dashboard/<int:user_id>", user_homepage, name="user-homepage"),
    # path("polls/<int:poll_id>/", poll_detail, name="poll-detail"),

]