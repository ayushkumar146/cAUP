from django.urls import path
from dashboard.views import user_homepage,contact_page,contact_view

urlpatterns = [
    path("Dashboard/<int:user_id>", user_homepage, name="user-homepage"),
    path('contact/<int:user_id>/', contact_page, name='contact-page'),
    # path('contact/<int:user_id>/', contact_page, name='contact-page'),
 
    # path("polls/<int:poll_id>/", poll_detail, name="poll-detail"),

]