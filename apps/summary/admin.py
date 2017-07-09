from django.contrib import admin

from .models import Summary


@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('site', 'value_a', 'value_b', 'created_at')
    list_filter = (('site', admin.RelatedOnlyFieldListFilter),)
