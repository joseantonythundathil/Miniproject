from django.db import models


class UserTable(models.Model):
	name=models.CharField(max_length=120,null=False)
	password=models.CharField(max_length=120,null=False)
	email=models.EmailField(max_length=200,null=False,unique=True)
	mobile=models.IntegerField(null=False)
	
	def __unicode__(self):
		return self.email 
