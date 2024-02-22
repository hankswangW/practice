from collections import defaultdict
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import numpy as np



def get_vaccine_data(id):    
    output=[]    
    temp=[]    
    with open("20230914.csv", 'r', encoding='gbk') as file:
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
       
##get_vaccine_data("V1")

'''
第一个方程去读取csv文件，把相同的预测Id的日期提出来，用字典找到每个日期出现的次数，并且最后按时间日期排序。
我简单看了一下，时间基本是全的，可能有几天的数据缺失，但不影响因为是按照日期排的。

'''


def func(id, seq, ratio):
       
    vaccine_data = get_vaccine_data(id)
    
    ## 第一段按照ratio打出标签
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

'''
第二个方程根据疫苗数量打出相应的标签，建立后面的模型
根据ratio得到一个比值list
'''


## 线性回归模型
data,ratio= func("V7",3,0.1)
data = np.array(data)
x=[]
y=[]
for i in range(len(data)):
    features = data[i][:3]
    label = data[i][-1]
    x.append(features)
    y.append(label)
# (80% 训练，20% 测试)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# 创建并训练线性回归模型
model = LinearRegression()
model.fit(X_train, y_train)

# 在测试集上进行预测
predictions = model.predict(X_test)

rounded_predictions = np.round(predictions)

# 计算准确度
accuracy = accuracy_score(y_test, rounded_predictions)

print("预测准确度：", accuracy)