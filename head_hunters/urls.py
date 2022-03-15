from django.urls import path
from . import views


app_name = 'head_hunters'
urlpatterns = [
    path('', views.index, name='index'),
    path('topics', views.topics, name='topics'),
    path('topic/<int:topic_id>', views.topic, name='topic'),
    path('new_topic', views.new_topic, name='new_topic'),
    path('new_summary/<int:topic_id>/', views.new_summary, name='new_summary'),
    path('edit_summary/<int:summary_id>', views.edit_summary, name='edit_summary'),
    path('new_vacancy/<int:topic_id>/', views.new_vacancy, name='new_vacancy'),
    path('edit_vacancy/<int:vacancy_id>', views.edit_vacancy, name='edit_vacancy'),
]