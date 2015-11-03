from datetime import datetime
from django.http import HttpResponse

from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from django.core import serializers
from django.core.urlresolvers import reverse

from django.db.models import Max
import json

from .mixins import LoginRequiredMixin
from .models import *

def all_json_models(request, feature):
                current_brand = Features.objects.get(featureclasskey=feature)
                print current_brand.featureclasskey
		print current_brand.featureclassname
                models = Parameterstable.objects.raw('select fews.parameterstable.id, fews.parameterstable.name,fews.parameterstable.groupkey,fews.parametergroups.unit,fews.parameterstable.parameterkey  from fews.parameterstable INNER JOIN fews.parametergroups ON (fews.parameterstable.groupkey = fews.parametergroups.groupkey) where fews.parameterstable.featureclasskey=%s'%(current_brand.featureclasskey))
                
                print models
                for i in models:
                                print i.unit

                json_models = serializers.serialize("json", models)
                return HttpResponse(json_models, content_type="application/javascript")

class IndexView(TemplateView):
	template_name = 'dashboard.html'


class DataForm(LoginRequiredMixin, TemplateView):
	template_name = 'dataform.html'


	def get_context_data(self, **kwargs):
		context = super(DataForm, self).get_context_data(**kwargs)
		features = Features.objects.all()
		locations = Locations.objects.all()
		parameters_list = Parameterstable.objects.all()
		context.update(locals())
		return context


def submit(request):
	postdata = request.POST.copy()
	print 'POSTDATA:'
	#print postdata
	param=(str(postdata['parameter']))
	q1 = Parameterstable.objects.filter(id=param)
	q1_values = list(q1.values())
	for x in q1_values:
		gk_id = x['groupkey_id']

	q2 = Parametergroups.objects.filter(groupkey=gk_id)
	q2_values = list(q2.values())
	for y in q2_values:
		unit = y['unit']
	print unit

	p = dict(postdata)
	#print type(p)
	for k,v in p.items():
		if v == 'parameter' and v == 'location':
			del p[v]
	#print p
	values_json = json.dumps(p, separators=(',',':'))
	#print values_json
	#current_id = Submissions.objects.all().aggregate(Max('id'))['id__max']

	data_submission = Submissions(
		parameter_id=postdata['parameter'],
		value_entries=values_json,
		location_id=postdata['location'],
		unit = unit
		)
	data_submission.save()
	
	messages.success(request, "Record added")
	return redirect('data_form')

	'''
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
	'''
	return redirect(reverse('data_form'))
