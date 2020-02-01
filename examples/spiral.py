# Inspiration: https://www.dataquest.io/blog/climate-temperature-spirals-python/

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import gif

%matplotlib inline

# cleaning code

df = pd.read_csv('examples/2410000301-eng.csv', skiprows=6)
df = df.drop(0).head(5).T.reset_index()
df = pd.DataFrame(df.values[1:], columns=df.iloc[0])
df = df.rename(columns={'Country of residence': 'month'})
df['month'] = pd.to_datetime(df['month'])
df = df.set_index('month')
df = df.apply(lambda x: x.str.replace(',', '')).apply(pd.to_numeric)
df = pd.DataFrame(df.apply(sum, axis=1)).reset_index()
df.columns = ['date', 'value']
df['year'] = df.date.dt.year
df['month'] = df.date.dt.month
df = df[df['year'] >= 1990]

@gif.frame
def plot_spiral(i):

i = 100
# initial plot setup
fig = plt.figure(figsize=(5, 5), dpi=100)
ax = plt.subplot(111, projection='polar')
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1) # for clockwise
ax.set_ylim(0, df['value'].max() * 1.1)
# month labels
lines, labels = ax.set_thetagrids(
    angles=(0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330),
    labels=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
)
ax.axes.get_yaxis().set_ticklabels([])
ax.axes.get_xaxis().set_ticklabels(labels)
ax.grid(False)
ax.set_facecolor('#000100')
ax.set_title(f"Visitors to Canada ({df['year'][i:i+1].values[0]})\n",
    color='#000100', fontdict={'fontsize': 15})
# grid lines
ax.plot(thetas, [l1] * t, c='#323331')
ax.plot(thetas, [l2] * t, c='#323331')
ax.plot(thetas, [l3] * t, c='#323331')
ax.text(np.pi/2, l1+l1/10, f"{l1/1e6}M", color="white", ha='center', fontdict={'fontsize': 10})
ax.text(np.pi/2, l2+l1/10, f"{l2/1e6}M", color="white", ha='center', fontdict={'fontsize': 10})
ax.text(np.pi/2, l3+l1/10, f"{l3/1e6}M", color="white", ha='center', fontdict={'fontsize': 10})
# actual data
ax.plot(df['month'][:i], df['value'][:i], color='red')

theta = dict(zip(range(1, 12+1), np.linspace(0, 2*np.pi, 12)))
df['month'] = df['month'].replace(theta)

frames = []
for i in range(df.shape[0]):
# for i in range(20):
    frame = plot_spiral(i)
    frames.append(frame)

gif.save(frames, 'examples/canada.gif', duration=50)

#

fig = plt.figure(figsize=(5, 5), dpi=100)
fig.set_facecolor("#323331")
ax = plt.subplot(111, projection='polar')
ax.plot(thetas, [l1] * t, c='#323331')
ax.plot(thetas, [l2] * t, c='#323331')
ax.plot(thetas, [l3] * t, c='#323331')
ax.text(np.pi/2, l1+l1/10, f"{l1/1e6}M", color="white", ha='center', fontdict={'fontsize': 10})
ax.text(np.pi/2, l2+l1/10, f"{l2/1e6}M", color="white", ha='center', fontdict={'fontsize': 10})
ax.text(np.pi/2, l3+l1/10, f"{l3/1e6}M", color="white", ha='center', fontdict={'fontsize': 10})
ax.plot(df['month'][:i], df['value'][:i], color='red')
ax.set_title("Visitors to Canada (1972 to 2019)", color='white', fontdict={'fontsize': 10})
ax.set_ylim(0, df['value'].max() * 1.1)
lines, labels = ax.set_thetagrids((0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330), labels=('Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
ax.axes.get_yaxis().set_ticklabels([])
ax.axes.get_xaxis().set_ticklabels(labels)
ax.grid(False)
ax.set_facecolor('#000100')





##
