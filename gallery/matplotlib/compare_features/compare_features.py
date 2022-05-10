# For more information on this animation check out the full tutorial on Medium:
# https://towardsdatascience.com/creating-beautiful-gif-with-python-for-your-data-analysis-ac50c618b559

import gif

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("gallery/matplotlib/compare_features/compare_features.csv")
df = df.rename(columns={"time": "date"})
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", drop=True, inplace=True)
df = df.resample("M").mean()

@gif.frame
def plot(df, date):
    df = df.loc[df.index[0] : pd.Timestamp(date)]
    fig, ax1 = plt.subplots(1, figsize=(5, 3), dpi=100)
    ax1.plot(
        df.temperature,
        color="tab:orange",
        marker="o",
        linestyle="--",
        linewidth=1,
        markersize=3,
    )
    ax1.set_ylabel("TEMPERATURE", color="tab:orange")
    ax2 = ax1.twinx()
    ax2.plot(
        df.visibility,
        color="tab:blue",
        marker="o",
        linestyle="--",
        linewidth=1,
        markersize=3,
    )
    ax2.set_ylabel("VISIBILITY", color="tab:blue")
    plt.title("Temperature vs Visibility")

frames = []
for date in pd.date_range(start=df.index[0], end=df.index[-1], freq="1M"):
    frame = plot(df, date)
    frames.append(frame)

gif.save(frames, "gallery/matplotlib/compare_features/compare_features.gif", duration=0.5, unit="s")