from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests, string, random
from coupoun.models import Gencode
from coupoun.forms import Codeform
from django.contrib import messages
from pathlib import Path
import requests

def info(request):
	response = requests.get('http://127.0.0.1:8000/apiview/')
	data=response.json()
	return render(request, 'coupoun/templates/home.html',{'data': data})

def test(request):
	response=requests.get('http://127.0.0.1:8000/apiview/')
	data = response.json()
	for i in data:
		x=i['total_donated']
		if(x>=3):
			result=1
		else:
			result=0
		if(x>=7):
			result=2
		elif(x<10 and x>=7):
			result=1
		else:
			result=0
		if(x>10):
			result=3
		elif(x<10 and x>=7):
			result=2
		elif(x<7 and x>=3):
			result=1
		else:
			result=0
		q="OER"
		w="OERIP"
		e="OERIPLO"
		if result == 0:
			user= str(i['user'])+'_'+str(result)+'_'+str(q)+'_'+str(w)+'_'+str(e)
			print(user)
			url='http://127.0.0.1:8000/profile_edit/'+user
			requests.put(url)
		if result == 1:
			if(i['code1'] == "OER"):
				code1=''.join(random.choices(string.ascii_uppercase+string.digits, k=3))
				code=Gencode(code=str(code1),codee="OERIP",codeee="OERIPLO")
				code.save()
				user=str(i['user'])+'_'+str(result)+'_'+str(code1)+'_'+str(w)+'_'+str(e)
				print(user)
				url='http://127.0.0.1:8000/profile_edit/'+user
				requests.put(url)
			else:
				user=str(i['user'])+'_'+str(result)+'_'+str(i['code1'])+'_'+str(i['code2'])+'_'+str(i['code3'])
				print(user)
				url='http://127.0.0.1:8000/profile_edit/'+user
				requests.put(url)
		if result == 2:
			if(i['code2'] == "OERIP"):
				code2=''.join(random.choices(string.ascii_uppercase+string.digits, k=5))
				code=Gencode(code=str(i['code1']),codee=str(code2),codeee="OERIPLO")
				code.save()
				user=str(i['user'])+"_"+str(result)+'_'+str(i['code1'])+'_'+str(code2)+'_'+str(e)
				print(user)
				url='http://127.0.0.1:8000/profile_edit/'+user
				requests.put(url)
			else:
				user=str(i['user'])+'_'+str(result)+'_'+str(i['code1'])+'_'+str(i['code2'])+'_'+str(i['code3'])
				print(user)
				url='http://127.0.0.1:8000/profile_edit/'+user
				requests.put(url)
		if result == 3:
			if(i['code3'] == "OERIPLO"):
				code3=''.join(random.choices(string.ascii_uppercase+string.digits, k=7))
				code=Gencode(code=str(i['code1']),codee=str(i['code2']),codeee=str(code3))
				code.save()
				user=str(i['user'])+'_'+str(result)+'_'+str(i['code1'])+'_'+str(i['code2'])+'_'+str(code3)
				print(user)
				url='http://127.0.0.1:8000/profile_edit/'+user
				requests.put(url)
			else:
				user=str(i['user'])+'_'+str(result)+'_'+str(i['code1'])+'_'+str(i['code2'])+'_'+str(i['code3'])
				print(user)
				url='http://127.0.0.1:8000/profile_edit/'+user
				requests.put(url)
	return redirect('info')

def entercode(request):
	if request.method == 'POST':
		form=Codeform(request.POST)
		if form.is_valid():
			urg = Gencode.objects.filter(code=form.cleaned_data['code'])
			urge = Gencode.objects.filter(codee=form.cleaned_data['code'])
			urgen = Gencode.objects.filter(codeee=form.cleaned_data['code'])
			if(urge.count() == 0 and urg.count() == 0 and urgen.count() == 0):
				messages.success(request, f'Enter a valid coupon code')
			if(urg.count() == 1):
				messages.success(request, f'Enjoy 30% off on your next purchase from Amazon')
			if(urge.count() == 1):
				messages.success(request, f'Enjoy 50% off on your next purchase from Amazon')
			if(urgen.count() == 1):
				messages.success(request, f'Enjoy 70% off on your next purchase from Amazon')
			context={'urg': urg,'urge':urge,'urgen':urgen }
			return render(request, 'coupoun/templates/rewards.html',context)
	else:
		form=Codeform()
	context={'form':form }
	return render(request, 'coupoun/templates/homeu.html', context)

