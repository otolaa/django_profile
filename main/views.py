from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class MainView(TemplateView):
    """ ICONS - Bootstrap """
    template_name = "main/main_list.html"

    @staticmethod
    def get_items_icon() -> list:
        return [
            'bi-asterisk',
            'bi-at',
            'bi-balloon-heart-fill',
            'bi-bar-chart-fill',
            'bi-arrow-through-heart-fill',
            'bi-apple',
            'bi-bicycle',
            'bi-box2-heart',
            'bi-balloon-fill',
            'bi-basket2-fill',
            'bi-dice-5-fill',
            'bi-alarm-fill',
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_list'] = self.get_items_icon()
        return context 