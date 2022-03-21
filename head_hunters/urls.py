from django.urls import path
from . import views


app_name = 'head_hunters'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topic/<slug:topic_slug>', views.topic, name='topic'),
    path('new_topic', views.new_topic, name='new_topic'),

    path('new_summary/<slug:topic_slug>/', views.new_summary,
        name='new_summary'),
    path('edit_summary/<int:summary_id>', views.edit_summary,
        name='edit_summary'),
    path('show_summary/<int:summary_id>', views.show_summary,
        name='show_summary'),
    path('delete_summary/<int:summary_id>', views.delete_summary,
        name='delete_summary'),

    path('new_vacancy/<slug:topic_slug>/', views.new_vacancy,
        name='new_vacancy'),
    path('edit_vacancy/<int:vacancy_id>', views.edit_vacancy,
        name='edit_vacancy'),
    path('show_vacancy/<int:vacancy_id>', views.show_vacancy,
        name='show_vacancy'),
    path('delete_vacancy/<int:vacancy_id>', views.delete_vacancy,
        name='delete_vacancy'),
]
