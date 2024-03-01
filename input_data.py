from collections import defaultdict,OrderedDict
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split 

def get_months(id): 
    output=[]    
    temp=[]    
    with open("practice/20230904-月度报表建模数据库.csv", 'r', encoding='gbk') as file:
        lines = file.readlines()
        for line in lines:
            columns = line.rstrip().split(',')                       
            output.append(columns)
        del(output[0])
        ##print(output[:10])    
        for data in output:
            if data[9] == id:
                temp.append(data[2:4])               
        ##print(len(temp))       
        date_count = defaultdict(int)  
        for year, month in temp:
            year = int(year)
            month = int(month)
            date_count[(year, month)] += 1
        sorted_dates = dict(sorted(date_count.items(), key=lambda x: (x[0][0], x[0][1])))
        ##print(sorted_dates)   
        values_list = list(sorted_dates.values())
        ##print(len(values_list))
    
    return values_list


def read_months_for_analyse(id: str, seq: int, ratio: float) -> list:
       
    vaccine_data = get_months(id)   
    result = []
    # 打标签
    for i in range(len(vaccine_data) - seq):
        x = vaccine_data[i:i+seq]  
        y = vaccine_data[i+seq]    
        avg = sum(x) / len(x)      
        if y >= avg * (1 - ratio) and y <= avg * (1 + ratio):
            result.append(x + [1]) 
        else:
            result.append(x + [0])      
            
    ##第二段按照seq求比值
    ratios = []
    for i in range(seq, len(vaccine_data)):
        avg_first_five_months = sum(vaccine_data[i-seq:i]) / seq
        sixth_month_value = vaccine_data[i]
        ratio = avg_first_five_months / sixth_month_value
        ratios.append(ratio)
    
    return result, ratios   


def get_days(id):
    output=[]    
    temp=[]    
    with open("practice/20230914 门诊每日接种流水数据库.csv", 'r', encoding='gbk') as file:
        lines = file.readlines()
        for line in lines:
            columns = line.rstrip().split(',')                       
            output.append(columns)
        del(output[0])
        ##print(output[:10])    
        for data in output:
            if data[8].strip('"') == id:
                temp.append(data[10])               
        #print(len(temp))   
    date_counts = defaultdict(int)
    for date in temp:
        date_counts[date] += 1
    sorted_date = dict(sorted(date_counts.items()))
    value_list= list(sorted_date.values())
    #print(len(value_list))
    return value_list

def read_days_for_analysis(id: str, seq: int) -> list:
           
    vaccine_data = get_days(id)
    
    ### 第一段按照ratio打出标签
    result = []
    for i in range(len(vaccine_data) - seq):
        x = vaccine_data[i:i+seq]  
        y = vaccine_data[i+seq]    
        avg = sum(x) / len(x)      
        if y >= avg * (1 - ratio) and y <= avg * (1 + ratio):
            result.append(x + [1]) 
        else:
            result.append(x + [0])  
        
    ##第二段按照seq求比值
    ratios = []
    for i in range(seq, len(vaccine_data)):
        avg_first_five_months = sum(vaccine_data[i-seq:i]) / seq
        sixth_month_value = vaccine_data[i]
        ratio = avg_first_five_months / sixth_month_value
        ratios.append(ratio)
    
    return result, ratios