from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('questions/',views.get_all_questions,name='get_all_questions'),
    path('questions/<int:question_id>/',views.get_question,name='get_question'),
    path('questions/create/',views.create_question,name='create_question'),
    path('questions/<int:question_id>/update/',views.update_question,name='update_question'),
    path('questions/<int:question_id>/delete/',views.delete_question,name='delete_question'),
]