from __future__ import unicode_literals
from django.db import models
# -*- coding: utf-8 -*-


class AccessToken(models.Model):
	token = models.CharField(max_length=30)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		get_latest_by = 'created_at'

	def __str__(self):
		return self.token
# Create your models here.
	# customers details
class Customer(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	phone = models.CharField(max_length=20)

	def __str__(self):
		return f'{self.firstname} {self.lastname}'

class Game(models.Model):
	opponent = models.CharField(max_length=100)
	Date= models.DateField((u"Conversation Date"), blank=True)
	Time = models.TimeField((u"Conversation Time"), blank=True)