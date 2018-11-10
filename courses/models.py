from django.db import models

# Create your models here.
class CourseList(models.Model):
    pass

class Course(models.Model):
    course_name = models.TextField()
    course_number = models.TextField(default='')
    semester = models.TextField(default='')
    instructor = models.TextField(default='')
    # course_list = models.ForeignKey(CourseList, default=None)
