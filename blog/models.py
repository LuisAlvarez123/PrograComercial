from django.db import models

# Create your models here.
from django.utils import timezone


class Publicacion(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fheca_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Publicaciones'
        
        