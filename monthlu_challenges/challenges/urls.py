from django.urls import path

from . import views

urlpatterns=[
    path('<int:month>', views.monthly),
    path('<str:month>', views.monthly_challenge_by_name,name='month-challenge')
]
