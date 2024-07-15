from django.contrib import admin
from .models import Department,Doctors,Booking,Contact,Login,Pharmacy

# Register your models here.

admin.site.register(Department)
admin.site.register(Doctors)
admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(Login)
admin.site.register(Pharmacy)

