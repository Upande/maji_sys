from datetime import datetime

from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from django.db.models import Max
from django.http import HttpResponse

from datetime import *

from .mixins import LoginRequiredMixin
from .models import *

import json


def all_json_models(request, feature):
                current_brand = Features.objects.get(featureclasskey=feature)
                print current_brand.featureclasskey
		print current_brand.featureclassname
                models = Parameterstable.objects.raw('select fews.parameterstable.id, fews.parameterstable.name,fews.parameterstable.groupkey,fews.parametergroups.unit,fews.parameterstable.parameterkey  from fews.parameterstable INNER JOIN fews.parametergroups ON (fews.parameterstable.groupkey = fews.parametergroups.groupkey) where fews.parameterstable.featureclasskey=%s'%(current_brand.featureclasskey))
                
                '''
                print models
                for i in models:
                                print i.unit
                				'''
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
	print postdata
	
	try:
		i = 0
		first_readings = postdata.getlist('reading1')
		second_readings = postdata.getlist('reading2')
		for x in first_readings:	
			d = postdata.getlist('date')[i]
			e = datetime.strptime(d, '%Y-%m-%d')
			reading1 = e + timedelta(hours=9)
			reading2 = e + timedelta(hours=16)
			v1 = postdata.getlist('reading1')[i]
			v2 = postdata.getlist('reading2')[i]
			flag = postdata.getlist('quality')[i]
			first_readings_submissions = Dump(
				date = reading1,
				value = float(v1),
				parameterid = postdata['parameter'],
				locationid = postdata['location'],
				flag = int(flag),
				comment = postdata['description'] )
			first_readings_submissions.save()

			second_readings_submissions = Dump(
				date = reading2,
				value = float(v2),
				parameterid = postdata['parameter'],
				locationid = postdata['location'],
				flag = int(flag),
				comment = postdata['description'] )
			second_readings_submissions.save()
			i = i + 1
		
	
		messages.success(request, "Record added")
		return redirect('data_form')
	except:
		messages.warning(request, "OOPS! make sure you have selected a parameter before submission")
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
	#return redirect(reverse('data_form'))
