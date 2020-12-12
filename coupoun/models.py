from django.db import models

# Create your models here.
class Gencode(models.Model):
	code = models.CharField(max_length=3,default="OER")
	codee = models.CharField(max_length=5, default="OERIP")
	codeee = models.CharField(max_length=7, default="OERIPLO")
	def save(self, *args):
		super().save()
