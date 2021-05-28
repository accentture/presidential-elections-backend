
from django.urls import path

from . import views

app_name = 'candidates_app'

urlpatterns = [
    path('get-information-candidates/', views.RenderDataCandidate.as_view(), name = 'get_candidates'),

]

