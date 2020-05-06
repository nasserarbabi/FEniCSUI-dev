from django.db import models
from dashboard.models import projects

class AnalysisConfig(models.Model):
    project = models.OneToOneField(
        projects,
        on_delete=models.CASCADE,
        primary_key=True)
    mesh = models.TextField()
    visualizationMesh = models.TextField()
    config = models.TextField()
    result = models.TextField()

    def __str__(self):
        return self.project.name


class SolverResults(models.Model):
    project = models.OneToOneField(
    projects,
    on_delete=models.CASCADE,
    primary_key=True)
    result = models.TextField()

    def __str__(self):
        return self.project.name

class SolverProgress(models.Model):
    project = models.OneToOneField(
    projects,
    on_delete=models.CASCADE,
    primary_key=True)
    progress = models.TextField()

    def __str__(self):
        return self.project.name