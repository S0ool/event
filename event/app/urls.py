from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('events/<int:event_id>/', views.event_info, name='event_info'),
    path('events/delete/<int:event_id>/', views.event_delete, name='delete_event'),
    path('participants/', views.participants, name='participants'),
    path('participants/<int:participant_id>/', views.participant_info, name='participant_info'),
    path('participants/delete/<int:participant_id>/', views.participant_delete, name='delete_participant'),
]
