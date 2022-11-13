from django.db import models


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Employee(AbstractPerson):
    position = models.CharField(max_length=30)
    salary = models.IntegerField(max_length=30)
    work_experience = models.CharField(max_length=100, null=True, blank=True)


class Passport(AbstractPerson):
    inn = models.IntegerField(max_length=30)
    id_card = models.IntegerField(max_length=30)
    person_data = models.OneToOneField(Employee, on_delete=models.CASCADE)


class WorkProject(models.Model):
    project_name = models.CharField(max_length=30)
    projects = models.ManyToManyField(Employee, through='Membership')


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()


class Client(AbstractPerson):
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)


class VipClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField(max_length=30)
