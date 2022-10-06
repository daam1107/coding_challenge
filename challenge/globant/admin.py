from django.contrib import admin
from .models import hired_employees
from .models import departments
from .models import jobs

admin.site.register(hired_employees)
admin.site.register(departments)
admin.site.register(jobs)
