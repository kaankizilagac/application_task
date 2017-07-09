from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.sites.models import Site

from .models import Summary


class ActiveMixin(object):
    active = ''

    def get_context_data(self, **kwargs):
        context = super(ActiveMixin, self).get_context_data(**kwargs)
        context['active'] = self.active
        return context


class SiteListView(ActiveMixin, ListView):
    template_name = 'sites/list.html'
    queryset = Site.objects.all().order_by('name')
    context_object_name = 'site_list'
    active = 'sites'


class SiteDetailView(ActiveMixin, DetailView):
    pk_url_kwarg = 'pk'
    queryset = Site.objects.prefetch_related('summaries')
    template_name = 'sites/detail.html'
    context_object_name = 'site'
    active = 'sites'


class SummaryView(ActiveMixin, TemplateView):
    active = 'summary'
    template_name = 'summary/sum.html'

    @staticmethod
    def get_sums():
        data = {}
        sum_list = Summary.objects.select_related('site')
        for summary in sum_list:
            site_id = summary.site_id
            exists = data.get(site_id, None)
            if not exists:
                data[site_id] = {
                    'site_name': summary.site.name,
                    'sum_of_value_a': summary.value_a,
                    'sum_of_value_b': summary.value_b
                }
                continue

            data[site_id]['sum_of_value_a'] += summary.value_a
            data[site_id]['sum_of_value_b'] += summary.value_b
        return data.values()

    def get_context_data(self, **kwargs):
        context = super(SummaryView, self).get_context_data(**kwargs)
        context['sum_list'] = self.get_sums()
        return context


class AverageView(ActiveMixin, TemplateView):
    active = 'summary'
    template_name = 'summary/avg.html'

    @staticmethod
    def get_avgs():
        #todo: siteye göre gruplayıp her bir sitenin value_a ve value_b sinin ortalamasını bul
        summary = Summary.objects.raw('SELECT site_id AS id, AVG(value_a), AVG(value_b) FROM summary_summary GROUP BY site_id')
        print(summary)
        return summary

    def get_context_data(self, **kwargs):
        context = super(AverageView, self).get_context_data(**kwargs)
        context['avg_list'] = self.get_avgs()
        context['active_btn'] = 'avg'
        return context
