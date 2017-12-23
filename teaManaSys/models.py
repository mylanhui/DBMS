from __future__ import unicode_literals

from django.db import models

# Create your models here.


class college(models.Model):
    collegeId = models.AutoField(primary_key=True)
    collegeName = models.CharField(max_length=20)

    def __unicode__(self):
        return self.collegeName

class major(models.Model):
    majorId = models.AutoField(primary_key=True)
    majorName =models.CharField(max_length=50)
    collegeId =models.ForeignKey(college,db_column="collegeId")

    def __unicode__(self):
        return self.majorName

class classList(models.Model):
    classId = models.AutoField(primary_key=True)
    className = models.CharField(max_length=12)
    studentNum = models.IntegerField()
    collegeId = models.ForeignKey(college, db_column="collegeId")
    majorId = models.ForeignKey(major, db_column="majorId")

    def __unicode__(self):
        return self.className

class teacher(models.Model):
    teacherId = models.CharField(primary_key=True,max_length=8)
    teacherName = models.CharField(max_length=10)
    teacherSex = models.BooleanField(default=0)
    collegeId = models.ForeignKey(college, db_column="collegeId")
    teacherTitle = models.CharField(max_length=20)

    def __unicode__(self):
        return self.teacherName

class courses(models.Model):
    coursesId =models.CharField(primary_key=True,max_length=8)
    coursesName =models.CharField(max_length=40)
    coursesTime =models.CharField(max_length=20)
    credit =models.IntegerField()
    teacherId =models.ForeignKey(teacher,db_column="teacherId")

    def __unicode__(self):
        return self.coursesName

class student(models.Model):
    studentId = models.CharField(primary_key=True,max_length=12)
    studentName = models.CharField(max_length=10)
    studentCourses = models.IntegerField()
    classId = models.ForeignKey(classList,db_column="classId")
    collegeId = models.ForeignKey(college, db_column="collegeId")
    majorId =models.ForeignKey(major,db_column="majorId")
    studentSex = models.BooleanField(default=0)
    coursesId = models.ManyToManyField(courses,db_column="coursesId")

    def __unicode__(self):
        return self.studentName

class grade(models.Model):
    gradeId = models.AutoField(primary_key=True)
    studentId =models.ForeignKey(student,db_column="studentId")
    coursesId =models.ForeignKey(courses,db_column="coursesId")
    score =models.CharField(max_length=10)

    def __unicode__(self):
        return self.gradeId

class User(models.Model):
    userId =models.CharField(primary_key=True,max_length=20)
    userName =models.CharField(max_length=20)
    password =models.CharField(max_length=16)

    def __unicode__(self):
        return self.userName