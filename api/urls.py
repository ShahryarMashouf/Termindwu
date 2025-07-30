from django.urls import path
from .views import TimeSlotListView, BookTimeSlotView

urlpatterns = [
    path('timeslots/', TimeSlotListView.as_view(), name='timeslot-list'),
    path('timeslots/<int:pk>/book/', BookTimeSlotView.as_view(), name='book-timeslot'),
]