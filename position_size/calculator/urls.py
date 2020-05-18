from calculator import views
from django.conf.urls import url

app_name = 'calculator'

urlpatterns = [
    url(r'^stocksize/', views.ResultView, name='result')
]
