from django.db import models
from datetime import date


class Job(models.Model):
    title = models.CharField(max_length=100)
    short_title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    national_id = models.CharField(max_length=25)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    main_salary = models.FloatField()

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name


class SalaryOthers(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='others')
    TYPE_CHOICES = (
        ('E', 'Earning'),
        ('D', 'Deduction'),
    )
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    date = models.DateField()
    amount = models.FloatField()

    def __str__(self):
        return self.title


class EarningManager(models.Manager):
    def get_queryset(self):
        return super(EarningManager, self).get_queryset().filter(
            type='E')

    def create(self, **kwargs):
        kwargs.update({'type': 'E'})
        return super(EarningManager).create(**kwargs)


class DeductionManager(models.Manager):
    def get_queryset(self):
        return super(DeductionManager, self).get_queryset().filter(
            type='D')

    def create(self, **kwargs):
        kwargs.update({'type': 'D'})
        return super(DeductionManager).create(**kwargs)


class Earnings(SalaryOthers):
    objects = EarningManager()

    class Meta:
        proxy = True


class Deductions(SalaryOthers):
    objects = DeductionManager()

    class Meta:
        proxy = True
