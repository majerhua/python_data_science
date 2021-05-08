import pandas as pd
import altair as alt
from altair_saver import save

alt.data_transformers.enable('json')
alt.renderers.enable('altair_saver', fmts=['vega-lite', 'png'])

url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/mpg/mpg.csv"
mpg = pd.read_csv(url)

chart = (alt.Chart(mpg)
         .encode(
    x='displ',
    y='hwy')
    .mark_circle()
)

save(chart, "chart.png")
