from django.contrib import admin

from rooms.models import *

class BlocoAdmin(admin.ModelAdmin):
    list_display = ('number_bloco',)
    search_fields = ('number_bloco',)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('bloco' ,'number_room','capacity','computers','board', )
    search_fields = ('bloco', 'number_room', 'capacity',)

admin.site.register(Room, RoomAdmin)
admin.site.register(Bloco, BlocoAdmin)