from django.db import models

from redactor.fields import RedactorField

# Create your models here.

class SobreNos(models.Model):
	titulo = models.CharField(u'Titulo', max_length=100)
	descricao = RedactorField(u'Descricao')

	class Meta:
		verbose_name = 'Sobre nos'
		verbose_name_plural = 'Sobre nos'

	def __str__(self):
		return self.titulo
