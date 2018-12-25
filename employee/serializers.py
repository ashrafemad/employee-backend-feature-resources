from rest_framework import serializers

from employee.models import Employee, Earnings, SalaryOthers, Deductions


class EmployeeSerializer(serializers.ModelSerializer):
    job_title = serializers.SerializerMethodField(read_only=True)
    earnings = serializers.SerializerMethodField()
    deductions = serializers.SerializerMethodField()

    def get_earnings(self, obj):
        return Earnings.objects.filter(employee=obj).values('date', 'amount')

    def get_deductions(self, obj):
        return Deductions.objects.filter(employee=obj).values('date', 'amount')

    def get_job_title(self, obj):
        return obj.job.title

    class Meta:
        fields = ('id', 'full_name', 'job_title', 'gender', 'age', 'country', 'date_of_birth', 'national_id', 'main_salary', 'earnings', 'deductions')
        model = Employee
