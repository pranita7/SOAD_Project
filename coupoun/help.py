from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests

def info(request):
    response = requests.get('http://127.0.0.1:8000/alldonatePosts/')
    data = response.json()
    return render(request, 'verify/home.html', {
        'data': data
    })

def test(request):
    response = requests.get('http://127.0.0.1:8000/alldonatePosts/')
    data = response.json()
    for i in data:
        print(i['is_requested'], i['is_acc_for_transport'])
        if i['is_requested'] == True and (i['is_acc_for_transport'] != True and i['is_acc_for_transport'] != False):
            print('hi')
            if(i['city']==i['to_city']):
                result = 'true'
            else:
                result = 'false'
            slug = i['slug']+'_'+result
            print(slug)
            url = 'http://127.0.0.1:8000/donatePostEdit/' + slug
            requests.put(url)
    #res = requests.put('http://127.0.0.1:8000/donatePostEdit/donation_true')
    return redirect('info')



    
        if result == 0:
            q = "OER"
            w = "OERIP"
            e = "OERIPLO"
            user = str(i['user'])+'_'+str(result)+'_'+str(q)+'_'+str(w)+'_'+str(e)
        if result == 1:
            code1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 3))

            #code = Gencode(code=str(code1),codee="OERIP",codeee="OERIPLO")
            ode.save()
            user = str(i['user'])+'_'+str(result)+'_'+str(code1)+'_'+"OERIP"+'_'+"OERIPLO"
        if result == 2:
            code1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 3))
            code2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
            code = Gencode(code=str(code1),codee=str(code2),codeee="OERIPLO")
            code.save()
            user = str(i['user'])+'_'+str(result)+'_'+str(code1)+'_'+str(code2)+'_'+"OERIPLO"
        if result == 3:
            code1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 3))
            code2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
            code3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 7))
            code = Gencode(code=str(code1),codee=str(code2),codeee= str(code3))
            code.save()
            user = str(i['user'])+'_'+str(result)+'_'+str(code1)+'_'+str(code2)+'_'+ str(code3)