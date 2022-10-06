from rest_framework import serializers

from .models import hired_employees
from .models import departments
from .models import jobs

class hired_employeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hired_employees
        fields = ('name', 'datetime', 'department_id', 'job_id')

class departmentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = departments 
        fields = ('department')

class jobsSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = jobs
        fields = ('job')