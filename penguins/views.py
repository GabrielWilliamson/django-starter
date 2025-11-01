from django.views.generic import TemplateView
from penguins.models import Penguin

class IndexView(TemplateView):
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["penguins"]= Penguin.objects.all()
        return context
