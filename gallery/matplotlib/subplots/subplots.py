import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O 
import seaborn as sns
import matplotlib.pyplot as plt
import gif
plt.style.use('fivethirtyeight')

# Data obtained from Kaggle
# anmidev/smart-meters-in-london?select=weather_hourly_darksky.csv
df=pd.read_csv('london_weather_hourly_darksky.csv')

#Renaming the time coloumn
df=df.rename(columns={"time": "date"})

#Converting it to the appropriate date format
df['date']=pd.to_datetime(df['date'])

#Indexing the date and droping the column
df.set_index('date',drop=True, inplace=True)

# Resampling on a monthly bases
df=df.resample('M').mean()

@gif.frame
def plot(df,date):
    
    df=df.loc[df.index[0]:pd.Timestamp(date)]
    fig, (ax1,ax2,ax3) = plt.subplots(3,figsize=(20,10),dpi=100)

    ax1.plot(df.temperature,marker='o', linestyle='--', linewidth=5,markersize=15, color='g')
    maxi=round(df.temperature.max()+5)
    ax1.set_title('SUBPLOTS',fontsize=30)
    ax1.set_xlim([START, END])
    ax1.set_ylim([0, maxi])
    ax1.set_ylabel('TEMPERATURE',color = 'green',fontsize=15)
    
    ax2.plot(df.visibility,marker='o', linestyle='--',    linewidth=5,markersize=15, color='r')
    maxi=round(df.visibility.max()+3)      
    ax2.set_xlim([START, END])
    ax2.set_ylim([0, maxi])
    ax2.set_ylabel('VISIBILITY',color = 'red',fontsize=15)
    
    ax3.plot(df.windSpeed,marker='o', linestyle='--', linewidth=5,markersize=15, color='b')
    maxi=round(df.windSpeed.max()+3)           
    ax3.set_xlim([START, END])
    ax3.set_ylim([0,maxi])
    ax3.set_ylabel('WINDSPEED',color = 'blue',fontsize=15)

##### CREATE ANIMATIONS ######
frames = []
for date in pd.date_range(start = df.index[0], end = df.index[-1],freq = '1M'):
    frame = plot(df,date)
    frames.append(frame)
gif.save(frames, "subplots.gif", duration=0.5 ,unit = 's')