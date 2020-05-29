from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/5/
    path('<int:pk>/', views.MbrQRAuth, name='MbrQRAuth'),
    # ex: /polls/5/results/
    path('getCert/',views.GenerateCertfication.as_view()),
]