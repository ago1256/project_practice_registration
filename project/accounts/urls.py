from django.urls import path
from .views import registration_step1, registration_step2

urlpatterns = [
    path('registration/', registration_step1, name='registration_step1'),
    path('registration/details/', registration_step2, name='registration_step2'),
] 