from django.contrib import admin
from core.models import LectureTicket

# Register your models here.


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(LectureTicket, TicketAdmin)