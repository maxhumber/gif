import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O 
import seaborn as sns
import matplotlib.pyplot as plt
import gif


#Data Source from KAggle: https://www.kaggle.com/jeanmidev/smart-meters-in-london
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
    
    fig, ax1 = plt.subplots(1,figsize=(5,3),dpi=100)
    
    ax1.plot(df.temperature, color = 'tab:orange',marker='o', linestyle='--', linewidth=1,markersize=3)
    ax1.set_ylabel('TEMPERATURE',color = 'tab:orange')
    ax2 = ax1.twinx()
    ax2.plot(df.visibility, color = 'tab:blue',marker='o', linestyle='--', linewidth=1,markersize=3)
    ax2.set_ylabel('VISIBILITY',color = 'tab:blue')
    plt.title('Temperature vs Visibility')

#### ANIMATION CREATION ####
frames = []
for date in pd.date_range(start = df.index[0], end = df.index[-1],freq = '1M'):
    frame = plot(df,date)
    frames.append(frame)
gif.save(frames, "compare_2_features.gif", duration=0.5 ,unit = 's')

# For more information on this animation check out the full tutorial on Medium:
# https://towardsdatascience.com/creating-beautiful-gif-with-python-for-your-data-analysis-ac50c618b559