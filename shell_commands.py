from employee.models import *
import datetime

Almaz = Employee.objects.create(name="Almazbek", birth_date="2001-01-10", position="junior", salary=500)
Atai = Employee.objects.create(name="Atai", birth_date="1998-11-16", position="middle", salary=900)
Aman = Employee.objects.create(name="Anamgeldi", birth_date="2000-03-29", position="team lid", salary=3000)
Askar = Employee.objects.create(name="Askarbek", birth_date="2001-08-07", position="senior", salary=2500)

Employee.objects.all()

ALmaz_passport = Passport.objects.create(name="Almaz Apazbekov", inn='21231231', birth_date="2001-01-10", id_card=1234, person_data=Almaz)
Atai_passport = Passport.objects.create(name="Atai Narynov", inn='2222123', birth_date="1998-01-10", id_card=1234, person_data=Atai)
Aman_passport = Passport.objects.create(name="Anam Tilenov", inn='1312124', birth_date="2000-01-10", id_card=1234, person_data=Aman)
Askar_passport = Passport.objects.create(name="Askar Dujsekeev", inn='16454124', birth_date="2007-01-10", id_card=1234, person_data=Askar)

Passport.objects.all()

ALmaz_passport.get_gender() #male
Aman_passport.get_gender() #female
Aman.get_age()

Askar.delete()


py_project = WorkProject(project_name="Codify project")
py_project.save()


Almaz_project_member = Membership(employee=Almaz, work_project=py_project, date_joined="2022-11-14")
Almaz_project_member.save()

Atai_project_member = Membership.objects.create(employee=Atai, work_project=py_project, date_joined="2022-11-14")
Aman_project_member = Membership.objects.create(employee=Aman, work_project=py_project, date_joined="2022-11-14")


# создать и добавить того, кого еще не было (вероятно надо как-то по другому)
Chyngyz = Employee.objects.create(name="Chika", birth_date="1992-06-17", position="senior", salary=2800)
Chyngyz_project_member = Membership.objects.create(employee=Chyngyz, work_project=py_project, date_joined="2022-11-14")


client_1 = Client.objects.create(address='djal', phone_number='0555-123-321', name='Almaz client', birth_date='2001-01-10')
client_2 = Client.objects.create(address='tunguch', phone_number='0775-154-532', name='Atai client', birth_date='1998-01-10')
client_3 = Client.objects.create(address='djal', phone_number='0700-765-234', name='Skar client', birth_date='2005-01-10')


vip_client = VipClient.objects.create(vip_status_start='2020-05-13', donation_amount=1300, address='djal', phone_number='0555-123-321',
                                      name='Aida VIP client', birth_date='1995-01-10')

Employee.objects.all()
Passport.objects.all()
WorkProject.objects.all()
WorkProject.objects.filter(projects__name__startswith='Almaz')
Client.objects.all()
VipClient.objects.all()


