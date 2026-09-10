import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

vegetables = {
    "Potato white": "potato_white.csv",
    "Tomato Nepali": "tomato_nepali.csv",
    "Onion Indian": "onion_indian.csv",
    "Cabbage": "cabbage.csv",
    "Mushroom": "mushroom.csv",

}

fig = make_subplots(
    rows=len(vegetables), 
    cols=1, 
    subplot_titles=list(vegetables.keys()),
    shared_xaxes=True,

    )

for i, (name, filename) in enumerate(vegetables.items(), start=1):
    df = pd.read_csv(filename)
    df["date"] = pd.to_datetime(df["date"])
    df["avg_price"] = df["avg_price"].astype(float)

    fig.add_trace(
        go.Scatter(x=df["date"], y=df["avg_price"], mode="lines", name=name),
        row=i, col=1
    )

fig.update_layout(
    title="Vegetable Price History",
    xaxis_title="Date",
    yaxis_title="Average Price (NPR)",
    height=800,
    width=1000,
    showlegend=True
)

fig.write_html("index.html")
fig.show()
print("Saved vegetable price history plot to vegetable_price_history.html")
