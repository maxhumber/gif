# For more information on this animation check out the full tutorial on Medium:
# https://towardsdatascience.com/creating-beautiful-gif-with-python-for-your-data-analysis-ac50c618b559

import gif

import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")


df = pd.read_csv("gallery/matplotlib/train_test_split/train_test_split.csv")
df = df.rename(columns={"time": "date"})
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", drop=True, inplace=True)
df = df.resample("M").mean()

END = df.index[-1]
START = df.index[0]


@gif.frame
def plot_split(df, date, split_date):
    df = df.loc[df.index[0] : pd.Timestamp(date)]
    fig, (ax1) = plt.subplots(1, figsize=(5, 3), dpi=100)
    if date < pd.Timestamp(split_date):
        ax1.axvspan(START, date, alpha=0.5, color="#33FF92")
        ax1.text(pd.Timestamp("2012-01-31"), y=12, s="TRAIN")
    if date > pd.Timestamp(split_date):
        ax1.axvspan(pd.Timestamp(split_date), date, alpha=0.5, color="#FCFF33")
        ax1.text(pd.Timestamp("2014-01-31"), y=12, s="TEST")
    ax1.plot(
        df.temperature,
        marker="o",
        linestyle="--",
        linewidth=1,
        markersize=3,
        color="tab:orange",
    )
    maxi = round(df.temperature.max() + 5)
    ax1.set_title("Train/Test-Split")
    ax1.set_xlim([START, END])
    ax1.set_ylim([0, maxi])
    ax1.set_ylabel("TEMPERATURE", color="tab:blue")


frames = []
for date in pd.date_range(start=df.index[0], end=df.index[-1], freq="1M"):
    frame = plot_split(df, date, "2013-06-21")
    frames.append(frame)

gif.save(
    frames,
    "gallery/matplotlib/train_test_split/train_test_split.gif",
    duration=0.5,
    unit="s",
)
