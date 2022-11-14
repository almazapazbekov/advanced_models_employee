from datetime import datetime, timedelta
from django.db import models


class AbstractPerson(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def get_age(self):
        year_now = datetime.now().year
        year_birth = self.birth_date.year
        return year_now - year_birth

    # def get_age(self):
    #     year_now = datetime.now().year
    #     year_birth = datetime(self.birth_date).year
    #     return year_now - year_birth


class Employee(AbstractPerson):
    position = models.CharField(max_length=30)
    salary = models.IntegerField()
    work_experience = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Пользователь {self.name} на должности {self.position} успешно сохранен')


class Passport(AbstractPerson):
    inn = models.CharField(max_length=30)
    id_card = models.IntegerField()
    person_data = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Паспорт {self.name} успешно сохранен. ИНН= {self.inn}')

    def get_gender(self):
        buffer = str(self.inn)
        if buffer.startswith('1'):
            gender = 'female'
        else:
            gender = 'male'

        return gender

    def __str__(self):
        return f'ФИО: {self.name} ИНН: {self.inn}, ID: {self.id_card}'


class WorkProject(models.Model):
    project_name = models.CharField(max_length=30)
    projects = models.ManyToManyField(Employee, through='Membership')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Проект {self.project_name} успешно создан')

    def __str__(self):
        return self.project_name


class Membership(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_project = models.ForeignKey(WorkProject, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'{self.employee} теперь член группы {self.work_project}. дата присоединения {self.date_joined}')


class Client(AbstractPerson):
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Адрес и номер телефона {self.name} успешно сохранен')


class VipClient(Client):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print(f'Вип клиент {self.name} успешно сохранен')
