import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ── CONFIG ──────────────────────────────────────────
vegetables = {
    "Potato White":  "potato_white.csv",
    "Tomato Nepali": "tomato_nepali.csv",
    "Onion Indian":  "onion_indian.csv",
    "Cabbage":       "cabbage.csv",
    "Mushroom":      "mushroom.csv",
}

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# ── CHART 1: LINE CHARTS (all vegetables) ───────────
fig_lines = make_subplots(
    rows=len(vegetables), cols=1,
    subplot_titles=list(vegetables.keys()),
    shared_xaxes=True
)

for i, (name, filename) in enumerate(vegetables.items(), start=1):
    df = pd.read_csv(filename)
    df["date"] = pd.to_datetime(df["date"])
    df["avg_price"] = df["avg_price"].astype(float)
    fig_lines.add_trace(
        go.Scatter(x=df["date"], y=df["avg_price"], mode="lines", name=name),
        row=i, col=1
    )

fig_lines.update_layout(title="Nepal Vegetable Price Trends", height=1500)
fig_lines.write_html("index.html")
print("Saved index.html")

# ── CHART 2: HEATMAPS (one per vegetable) ───────────
for name, filename in vegetables.items():
    df = pd.read_csv(filename)
    df["date"] = pd.to_datetime(df["date"])
    df["avg_price"] = df["avg_price"].astype(float)
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year

    pivot = df.pivot_table(
        values="avg_price", index="month", columns="year", aggfunc="mean"
    )

    fig_heat = go.Figure(data=go.Heatmap(
        z=pivot.values,
        x=[str(c) for c in pivot.columns],
        y=[month_names[m-1] for m in pivot.index],
        colorscale="RdYlGn_r",
        text=pivot.values.round(1),
        texttemplate="%{text}",
        hoverongaps=False,
    ))

    fig_heat.update_layout(
        title=f"{name} — Monthly Price Heatmap (Rs/kg)",
        xaxis_title="Year",
        yaxis_title="Month",
    )

    out = name.lower().replace(" ", "_") + "_heatmap.html"
    fig_heat.write_html(out)
    print(f"Saved {out}")

print("All charts done.")