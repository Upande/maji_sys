from datetime import datetime
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core import serializers
from django.core.urlresolvers import reverse

from django.db.models import Max

from .mixins import LoginRequiredMixin
from .models import *

def all_json_models(request, feature):
                current_brand = Features.objects.get(featureclasskey=feature)
                print current_brand.featureclasskey
		print current_brand.featureclassname
                models = Parameterstable.objects.raw('select * from fews.parameterstable where featureclasskey=%s'%(current_brand.featureclasskey))
                json_models = serializers.serialize("json", models)
                return HttpResponse(json_models, content_type="application/javascript")

class IndexView(TemplateView):
	template_name = 'dashboard.html'


class DataForm(LoginRequiredMixin, TemplateView):
	template_name = 'dataform.html'

	def get_context_data(self, **kwargs):
		context = super(DataForm, self).get_context_data(**kwargs)
		features = Features.objects.all()
		print features
		for f in features:
			print f
		locations = Locations.objects.all()
		parameters_list = Parameterstable.objects.all()
		context.update(locals())
		return context


	def post(self, request, *args, **kwargs):
		postdata = request.POST.copy()
		print 'POSTDATA:'
		print postdata
		print 'LOCATION: {0}'.format(postdata['location'])
		readings = postdata.getlist('reading')
		remarks = postdata.getlist('remark')
		module_instance = Moduleinstances.objects.get(name='Data Entry Form')
		parameter = Parameterstable.objects.get(id=postdata['parameter'])
		time_step = Timesteps.objects.get(id='CTS_M')
		print module_instance.description

		current_id = Timeserieskeys.objects.all().aggregate(Max('serieskey'))['serieskey__max']

		entry_date_time = datetime.now()
		print request.user
		try:
			time_series_key = Timeserieskeys(
				serieskey=current_id+1,
				locationkey=postdata['location'],
				parameterkey=parameter,
				moduleinstancekey=module_instance,
				timestepkey=time_step,
				valuetype=0,
				modificationtime=entry_date_time
			)
			time_series_key.save()


			i = 1
			y = 0
			for reading in readings:
				dt=datetime(year=int(postdata['year']), month=int(postdata['month']), day=int(postdata['day']), hour=int(postdata['time']))
				time_series_manual_edits_history = Timeseriesmanualeditshistory(
					serieskey=time_series_key,
					editdatetime=entry_date_time,
					datetime=dt,
					#userkey=request.user,
					userkey=1,
					scalarvalue=float(readings[y]),
					flags=0,
					commenttext=str(remarks[y])
				)
				time_series_manual_edits_history.save()
				print 'Reading: {0}   Remarks:{1}'.format(readings[y], remarks[y])

				y = y+1
				print 'data saved'

		except Exception as ex:
			print 'exception: {0}'.format(ex.message)

		return redirect(reverse('data_form'))
