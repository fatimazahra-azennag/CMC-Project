from django.shortcuts import render
from django.http import HttpResponse


from .models import Transition
from .models import Userfiles
from django.db.models import Count
from django.utils import timezone
from django.db.models.functions import Trunc
from django.db.models import Q
from django.db.models import F
import pandas as pd
import json
from datetime import date


# Create your views here.

def index(request):
    labelsChart = []
    dataChart1 = []
    dataChart2 = []
    delai_mean = 0
    transitions = Transition.objects.filter(titre ='Répondre à un message')
    df = pd.DataFrame.from_records(transitions.values())
    df['idforum'] = df['attribut'].str.extract(r'IDForum=(\d+)')
  
    result=user_msg('17',df)
    fitered_result = result[['utilisateur','count_msg','delai_mean_msg']].drop_duplicates()
    delai_mean = result['delai_mean'].drop_duplicates()
    for value in fitered_result['utilisateur']:
        labelsChart.append(value)
    for value in fitered_result['count_msg']:
        dataChart1.append(value)
    for value in fitered_result['delai_mean_msg'] :
        dataChart2.append(value)
    print(result) 

    
    
    context ={
        'dataChart1':json.dumps(dataChart1),
        'labelsChart' :json.dumps(labelsChart),
        'dataChart2' :json.dumps(dataChart2),
        'delai_mean' :  delai_mean[0]
    }
    return render(request,'index.html',context)
def user_delai(idforum,df):
    filtered_df=df[(df['idforum']== idforum)]
    delai_mean = 0
    result = pd.DataFrame()
    for time in filtered_df['delai']:
        delai_mean+=time.hour*3600 + time.minute*60 + time.second
    delai_mean= delai_mean/ len(filtered_df['delai'])
    filtered_df['delai_mean'] = delai_mean
    result = pd.concat([result,filtered_df], ignore_index=True) 
    return result
def user_msg (idforum,df):
    result = user_delai(idforum,df)
    result1 = pd.DataFrame()
    user_distinct_values = result['utilisateur'].drop_duplicates()
    delai_mean = 0 
    for value in user_distinct_values :
        filtered_result = result[(result['utilisateur']== value)]
        delai_mean = 0 
        for time in filtered_result['delai'] :
            delai_mean+=time.hour*3600 + time.minute*60 + time.second
        delai_mean= delai_mean/ len(filtered_result['delai'])
        filtered_result['delai_mean_msg'] = delai_mean
        print(value,':count_msg:',len(filtered_result))
        filtered_result['count_msg'] = len(filtered_result)
        result1 = pd.concat([result1,filtered_result], ignore_index=True)
    return result1 
    
    


    

   