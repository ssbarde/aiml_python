import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('TE_final.csv')

print(df.head())

# print("fdfd")

print(df.columns)

a=df['Name'].apply(lambda x:x.split(' '))

df[a.apply(lambda x: 'GOTETI' in x)]

df = df.drop(labels=[114],axis=0)

print(df.info())

df1 = df[['310241', '310242', '310243', '310244', '310245',
       '310246 TW', '310246 PR', '310247 TW', '310247 PR', '310248 TW',
       '310248 PR', '310250', '310251', '310252', '310253', '310254',
       '310255 TW', '310256 TW', '310256 PR', '310257 TW', '310257 PR',
       '310258 TW', 'TY', 'SGPA', 'Total']]

print(df1[['TY', 'SGPA']].head())

df1.rename(columns={'TY':'SGPA','SGPA':'Total_Credits'},inplace=True)

l=['310241', '310242', '310243', '310244', '310245',
       '310246 TW', '310246 PR', '310247 TW', '310247 PR', '310248 TW',
       '310248 PR', '310250', '310251', '310252', '310253', '310254',
       '310255 TW', '310256 TW', '310256 PR', '310257 TW', '310257 PR',
       '310258 TW']

def marks(x):
    try:
        t=int(x.split('/')[0])
    except:
        t=0
    return t


for i in l:
    df1[i] = df1[i].apply(marks)
    
print(df1.head())

def credits(x):
    try:
        t=float(x.split(':')[1][:3])
    except:
        t=0
    return t

df1['Total_Credits'][0].split(':')[1][:3]

df1['Total_Credits'].apply(credits)
#credits('TOTAL CREDITS EARNED : 43 ..........CONFIDENT...')


df1['Total_Credits'] = df1['Total_Credits'].apply(credits)

print(df1['Total_Credits'])

def sgpa_float(x):
    try:
        t=float(x.split(':')[1][1:])
    except:
        t=3.9
    return t

sgpa_float(df1['SGPA'][121])

df1['SGPA']=df1['SGPA'].apply(sgpa_float)

df2 = df1.drop(['Total'],axis=1)

print(df2.head())

df2.info()

print(df2.head())

roll=np.arange(0,343)
plt.scatter(roll,df2['310241'],c='red')
plt.scatter(roll,df2['310242'],c='blue')

print(df2['310241'].hist())