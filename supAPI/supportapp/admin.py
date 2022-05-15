from django.contrib import admin

from supportapp import models


@admin.register(models.AppUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TicketQueue)
class QueueAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Messages)
class MessagesAdmin(admin.ModelAdmin):
    pass