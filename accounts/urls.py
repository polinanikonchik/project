from django.urls import path,include
from .views import Registration

urlpatterns = [
    path('registration', Registration.as_view(), name='accounts-registration')
]
