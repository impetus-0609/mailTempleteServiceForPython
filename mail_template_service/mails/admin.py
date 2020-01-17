from django.contrib import admin
from .models import (Employee, Unit, Team, Section, MailTemplete)

admin.site.register(Employee)
admin.site.register(Unit)
admin.site.register(Team)
admin.site.register(Section)
admin.site.register(MailTemplete)