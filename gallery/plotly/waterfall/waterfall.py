import gif

import pandas as pd
import plotly.graph_objects as go

df = pd.DataFrame(
    [
        [2016, 60, 80, 0, -40, -20, 0],
        [2017, 50, 30, 0, -30, -10, 0],
        [2018, 50, 40, 0, -30, -30, 0],
        [2019, 60, 50, 0, -30, -10, 0],
        [2020, 70, 60, 0, -50, -20, 0],
    ],
    columns=[
        "Year",
        "Sales",
        "Consulting",
        "Net revenue",
        "Purchases",
        "Other expenses",
        "Profit before tax",
    ],
)


@gif.frame
def plot(year):
    d = df[df["Year"] == year]
    fig = go.Figure(
        go.Waterfall(
            x=d.columns[1:],
            y=d.values[0][1:],
            measure=["relative", "relative", "total", "relative", "relative", "total"],
            name="20",
            orientation="v",
            textposition="outside",
            connector={"line": {"color": "rgb(63, 63, 63)"}},
        )
    )
    fig.update_layout(
        title=f"Profit and loss statement for {d.values[0][0]}",
        showlegend=False,
        yaxis={"range": [0, 200]},
        width=500,
        height=300,
        margin=dict(l=10, r=10, t=50, b=10),
    )
    return fig


frames = []
for year in range(2016, 2020 + 1):
    frame = plot(year)
    frames.append(frame)

gif.save(
    frames,
    "gallery/plotly/waterfall/waterfall.gif",
    duration=3,
    unit="seconds",
    between="startend",
)
