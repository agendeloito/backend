from django.db import models

# Create your models here.

class Schedule(models.Model):
    id_schedule = models.AutoField(primary_key=True,db_comment='id')
    title = models.CharField(max_length=20, blank=True, null=True)
    rut = models.CharField(max_length=20, blank=True, null=True)
    startdate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'schedule'


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=20,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'status'

class Employee(models.Model):
    
    rut = models.CharField(primary_key=True, max_length=10, unique=True,null=False)
    name = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    id_status = models.ForeignKey(Status, models.DO_NOTHING, db_column='id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    rol = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class Validation(models.Model):
    id = models.IntegerField(primary_key=True)
    rut = models.ForeignKey(Employee, models.DO_NOTHING, db_column='rut', blank=True, null=True)
    doc1 = models.IntegerField(blank=True, null=True)
    doc2 = models.IntegerField(blank=True, null=True)
    doc3 = models.IntegerField(blank=True, null=True)
    doc4 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validation'
