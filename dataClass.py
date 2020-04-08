import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from pandas import DataFrame


data=pd.read_csv('COVID19_open_line_list.csv')

data2=pd.read_csv('time_series_covid_19_confirmed.csv')


#인구별 확진자 비율(data2의 csv파일 사용)
plt.figure(figsize=(7,6))
sns.barplot(x=['Korea, South','Italy','France'],
            y=[10237/51470000,124632/60480000,89953/60900000])
plt.ylabel("% of population infected")
plt.xlabel("country")
plt.show()
'''
#한국의 누적 확진자 그래프(data2의 csv파일 사용)
plot_data=data2[data2['Country/Region']=='Korea, South'].sum().drop(['Province/State','Country/Region','Lat','Long'])
plt.figure(figsize=(15,5))
sns.barplot(plot_data.index,plot_data,palette='Blues')
plt.xticks(rotation=90)
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.title('Confirmed Cases in Korea, South over Time')
plt.show()


#연령별 확진,사망,완치(퇴원) 비율
def clean(x):
    if x== 'death' or x =='died' or x== 'Death':
        return 'death'
    elif x=='discharged'or x=='discharge':
        return 'discharge'
    elif x=='recovered' or x=='stable':
        return'recovered'
    else:
        return np.nan
def apply_int(x):
    try:
        y=int(x)
        return y
    except:
        return np.nan

plt.figure(figsize=(14,5))

sns.distplot(data[data['outcome'].apply(clean)=='death']
             ['age'].apply(apply_int),hist=False,rug=True,label='Deaths')
sns.distplot(data[data['outcome'].apply(clean)=='discharge']
             ['age'].apply(apply_int),hist=False,rug=True,label='Discharged')
sns.distplot(data[data['outcome'].apply(clean)=='recovered']
             ['age'].apply(apply_int),hist=False,rug=True,label='Recovered')
plt.legend()
plt.show()
'''






