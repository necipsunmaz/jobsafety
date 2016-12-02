from django.contrib import admin
from jobsafe.models import Team, TeamUser, Company


class TeamUserInline(admin.StackedInline):
    model = TeamUser
    extra = 0
    raw_id_fields = ("user",)
    list_display = ("job", "company")


class TeamAdmin(admin.ModelAdmin):
    inlines = [TeamUserInline,]
    raw_id_fields = ("manager",)
    list_display = ("name", "address")


admin.site.register(Team, TeamAdmin)