from django.db import models

from accounts.models import Create_user


class Position(models.Model):
    emp_position = models.CharField(max_length=40)
    branch = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.emp_position} - {self.branch}'


class Employee(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.IntegerField()
    create_user = models.ForeignKey(Create_user, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.position}'

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user.create_user)
