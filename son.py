
#plot_data=data2[data2['Country/Region']=='France']
#print(plot_data.head())
'''
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

plot_data=data2[data2['Country/Region']=='China'].sum().drop(['Province/State','Country/Region','Lat','Long'])
plt.figure(figsize=(15,5))
sns.barplot(plot_data.index,plot_data,palette='Blues')
plt.xticks(rotation=90)
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.title('Confirmed Cases in China over Time')
plt.show()

plot_data=data2[data2['Country/Region']=='Korea, South'].sum().drop(['Province/State','Country/Region','Lat','Long'])
plt.figure(figsize=(15,5))
sns.barplot(plot_data.index,plot_data,palette='Blues')
plt.xticks(rotation=90)
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.title('Confirmed Cases in Korea, South over Time')
plt.show()

plt.title('ltaly_date_Confirmed')
#축 이름 설정
plt.xlabel('ObservationDate')
plt.ylabel('Confirmed')
#범위 설정

#data.Confirmed.hist(bins=10)

plt.figure(figsize=(23,10))
plt.bar(data_france.ObservationDate,data_france.Confirmed,label="Confirmed")
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend(frameon=True,fontsize=12)
plt.title('Confirm',fontsize=30)
plt.show()s
'''