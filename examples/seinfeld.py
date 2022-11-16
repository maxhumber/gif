import re

import pandas as pd
from matplotlib import pyplot as plt

import gif

# script cleaning
df = pd.read_csv("gallery/data/seinfeld.csv")
df = df[df["character"].isin(["JERRY", "GEORGE", "ELAINE", "KRAMER"])]
df["character"] = df["character"].str.capitalize()
df["episode"] = df["episode"].apply(
    lambda x: float(f'{x.split("E")[0][1:]}.{x.split("E")[1]}')
)
df["line"] = df["line"].apply(lambda x: re.sub("(?<=\()(.*)(?=\))", "", x))
df["words"] = df["line"].apply(lambda x: len(re.findall("\w+", x)))
df = df.groupby(["episode", "character"])["words"].sum().reset_index()
df = df.sort_values(["episode", "character"])

# if character doesn't appear in episode...
df = df.set_index(["episode", "character"])
df = df.reindex(
    pd.MultiIndex.from_product(
        [df.index.levels[0], df.index.levels[1]], names=["episode", "character"]
    ),
    fill_value=0,
)
df = df.reset_index()

# calculate words in episode
wie = df.groupby(["episode"]).sum()
wie = wie.rename(columns={"words": "wie"})
wie["wie_cumsum"] = wie["wie"].cumsum()
wie = wie.reset_index()

# calculate character cumsum
df = pd.merge(df, wie, on=["episode"])
df["character_cumsum"] = df.groupby("character")["words"].cumsum()
df["%"] = df["character_cumsum"] / df["wie_cumsum"]
df["e%"] = df["words"] / df["wie"]
df = df[["episode", "character", "%", "e%"]]
df = df.sort_values(["episode", "%"])
df["episode"] = df["episode"].apply(
    lambda x: str(x) + "0" if len(str(x)) == 3 else str(x)
)

# colour mapping
colours = {
    "Jerry": "#0526E3",
    "George": "#7F8068",
    "Elaine": "#D1DE1F",
    "Kramer": "#E3C505",
}

df["color"] = df["character"].map(colours)


@gif.frame
def plot(episode):
    ep = df[df["episode"] == episode].copy()
    title = ep["episode"].values[0].split(".")
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(5, 3), dpi=100)
    # episode plot
    axes[0].barh(ep["character"], ep["e%"], color=ep["color"])
    axes[0].set_xlim([0, 1])
    axes[0].set_xticks([])
    axes[0].yaxis.set_tick_params(labelsize=10)
    axes[0].yaxis.set_ticks_position("none")
    axes[0].set_facecolor("#FFFFFF")
    axes[0].set_xlabel(f"Season {title[0]} Episode {int(title[1])}")
    # total plot
    axes[1].barh(ep["character"], ep["%"], color=ep["color"])
    axes[1].set_xlim([0, 1])
    axes[1].set_xticks([])
    axes[1].set_yticks([])
    axes[1].set_xlabel(f"Total")
    axes[1].set_facecolor("#FFFFFF")


frames = []
for episode in df.episode.unique():
    frame = plot(episode)
    frames.append(frame)

gif.save(frames, "images/seinfeld.gif", duration=100)
