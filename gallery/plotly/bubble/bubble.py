import gif

import plotly.graph_objects as go
import numpy as np

np.random.seed(1)

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sz = np.random.rand(N) * 30

layout = go.Layout(
    xaxis={"range": [-2, 2]},
    yaxis={"range": [-2, 2]},
    margin=dict(l=10, r=10, t=10, b=10),
)


@gif.frame
def plot(i):
    fig = go.Figure(layout=layout)
    fig.add_trace(
        go.Scatter(
            x=x[:i],
            y=y[:i],
            mode="markers",
            marker=go.scatter.Marker(
                size=sz[:i], color=colors[:i], opacity=0.6, colorscale="Viridis"
            ),
        )
    )
    fig.update_layout(width=500, height=300)
    return fig


frames = []
for i in range(100):
    frame = plot(i)
    frames.append(frame)

gif.save(frames, "gallery/plotly/bubble/bubble.gif")
