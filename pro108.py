import random
import plotly.figure_factory as ff
import csv
import pandas as pd


d = pd.read_csv("1.csv")
fig = ff.create_distplot([d["Avg Rating"].tolist()],["Mobile Brand avg rating"])
fig.show()