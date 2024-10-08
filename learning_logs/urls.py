"""Defines url petterns for learning logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [
    #home Page
    path('', views.index, name = 'index'),
    # Page that shows all topics.
    path('topics/', views.topics, name = 'topics'),
    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    # Page to add new topic
    path('new_topic/', views.new_topic, name = 'new_topic'),
    # Page to add new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Page to edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]