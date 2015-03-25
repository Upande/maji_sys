from django.views.generic import TemplateView

from .mixins import LoginRequiredMixin
from .models import *

class IndexView(TemplateView):
	template_name = 'dashboard.html'


class DataForm(LoginRequiredMixin, TemplateView):
	template_name = 'data_form.html'

	def get_context_data(self, **kwargs):
		context = super(DataForm, self).get_context_data(**kwargs)
		locations = Locations.objects.all()
		parameters_list = Parameterstable.objects.all()
		context.update(locals())
		return context