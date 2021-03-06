 ####
 # https://towardsdatascience.com/creating-beautiful-gif-with-python-for-your-data-analysis-ac50c618b559

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
def plot_split(df,date,split_date):
    
    df=df.loc[df.index[0]:pd.Timestamp(date)]
    fig, (ax1) = plt.subplots(1,figsize=(20,5),dpi=100)
    
    #TRAIN
    if date < pd.Timestamp(split_date):
        ax1.axvspan(START,date, alpha = 0.5, color = '#33FF92')
        ax1.text(pd.Timestamp('2012-01-31'),y=12,s = 'Train',fontsize=30)# where the train text goes
    #TEST
    if (date > pd.Timestamp(split_date)):
        ax1.axvspan(pd.Timestamp(split_date),date, alpha = 0.5,   color = '#F933FF')
        ax1.text(pd.Timestamp('2014-01-31'),y=12,s = 'Test',fontsize=30)
    ax1.plot(df.temperature,marker='o', linestyle='--', linewidth=5,markersize=15, color = 'tab:orange')
    maxi=round(df.temperature.max()+5)
    
    ax1.set_title('Train/Test-Split',fontsize=30)
    ax1.set_xlim([START, END])
    ax1.set_ylim([0, maxi])
    ax1.set_ylabel('TEMPERATURE',color = 'tab:blue',fontsize=30)


frames = []
for date in pd.date_range(start = df.index[0], end = df.index[-1],freq = '1M'):
    frame = plot_split(df,date,'2013-06-21')
    frames.append(frame)
gif.save(frames, "train_test_split.gif", duration=0.5 ,unit = 's')