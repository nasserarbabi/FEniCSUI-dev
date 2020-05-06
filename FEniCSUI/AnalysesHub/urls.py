from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from AnalysesHub import views

urlpatterns = [
    path('solverConfig/<uuid:project_id>', views.solverConfig.as_view()),
    path('categories/<uuid:project_id>', views.Categories.as_view()),
    path('getConfig/<uuid:project_id>', views.getConfiguration.as_view()),
    path('results/<uuid:project_id>', views.resutls.as_view()),
    path('solvers/<uuid:project_id>', views.solvers.as_view()),
    path('solverProgress/<uuid:project_id>', views.solverProgress.as_view()),

]