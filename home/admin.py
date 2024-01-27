from django.contrib import admin
from . import models

@admin.register(models.facility)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('instrument_name',)

admin.site.register(models.collaborator)
admin.site.register(models.home)
admin.site.register(models.about)
admin.site.register(models.centre)
admin.site.register(models.project)
admin.site.register(models.publication)
admin.site.register(models.patent)
admin.site.register(models.people)
admin.site.register(models.committee)
admin.site.register(models.committee_member)
admin.site.register(models.academic)
# admin.site.register(models.facility)
admin.site.register(models.news)
