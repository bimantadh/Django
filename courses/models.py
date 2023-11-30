from django.db import models


class Profile(models.Model):
	course_name = models.CharField(max_length=100)
	course_id = models.CharField(max_length=100)
	course_details = models.CharField(max_length=10000)
	course_duration = models.IntegerField()


	def __str__(self) -> str:
		return self.course_name
	