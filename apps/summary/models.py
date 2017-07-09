from django.db import models
from django.contrib.sites.models import Site
from django.utils.timezone import now


class Summary(models.Model):
    site = models.ForeignKey(to=Site, related_name='summaries')
    value_a = models.DecimalField(verbose_name='Value A', max_digits=7, decimal_places=3)
    value_b = models.DecimalField(verbose_name='Value B', max_digits=7, decimal_places=3)
    created_at = models.DateField(verbose_name='Created at', default=now, blank=True)

    def __str__(self):
        return '{}; A:{}, B:{}'.format(self.site.domain, self.value_a, self.value_b)

    class Meta:
        verbose_name = 'Summary'
        verbose_name_plural = 'Summaries'
