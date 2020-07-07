import gif
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("examples/canada.csv")
theta = dict(zip(range(1, 12 + 1), np.linspace(0, 2 * np.pi, 12)))
df["month"] = df["month"].replace(theta)


@gif.frame
def plot(i):
    # frame layout
    fig = plt.figure(figsize=(5, 5), dpi=100)
    ax = plt.subplot(111, projection="polar")
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)  # for clockwise
    ax.set_ylim(0, df["value"].max() * 1.1)
    ax.xaxis.grid()  # horizontal r lines
    ax.set_rticks([500_000, 1_000_000, 1_500_000])
    ax.set_yticklabels(["0.5M", "1.0M", "1.5M"], color="grey")
    # month labels
    lines, labels = ax.set_thetagrids(
        angles=(0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330),
        labels=(
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ),
    )
    ax.set_xticklabels(labels, fontdict={"fontsize": 9})
    # styling
    ax.set_facecolor("#000100")
    ax.set_title(
        f"Visitors to Canada ({df['year'][i:i+1].values[0]})\n",
        color="#000100",
        fontdict={"fontsize": 10},
    )
    # actual data
    ax.plot(df["month"][:i], df["value"][:i], color="red")


frames = []
for i in range(df.shape[0]):
    frame = plot(i)
    frames.append(frame)

gif.save(frames, "examples/canada.gif", duration=30)
