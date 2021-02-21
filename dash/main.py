import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import os


import pandas as pd
import numpy as np
import plotly.express as px

anxiety_by_age_12 = pd.read_csv ('./national_anxiety_by_age_12.csv')
age_fig_12 = px.bar(anxiety_by_age_12, x="Subgroup", y="Value", labels={
    "Value":"National Estimate of Anxiety(in percent)",
    "Subgroup":"Age Range"
}, title="Anxiety By Age Week 1 of COVID")


anxiety_by_age_1 = pd.read_csv('./national_anxiety_by_age_1.csv')
age_fig_1 = px.bar(anxiety_by_age_1, x="Subgroup", y="Value", labels={
    "Value":"National Estimate of Anxiety(in percent)",
    "Subgroup":"Age Range"
}, title="Anxiety By Age Week 1 of COVID")


df = pd.read_csv ('./anxiety.csv')
dfa = df[df['State'] == "United States"]
df_new = df[df['Subgroup'] == "United States"]

df_anxiety = df_new[df_new['Indicator'] == "Symptoms of Anxiety Disorder"]
df_depression = df_new[df_new['Indicator'] == "Symptoms of Depressive Disorder"]



fig1 = px.line(df_depression, x="Time Period Label", y="Value", color="Phase", template="simple_white", labels={
    "Value": "National Estimate of Depression(in percent)",
    "Time Period Label": "Time Period (2020)"
}, title="Depression Over Time")

fig2 = px.line(df_anxiety, x="Time Period Label", y="Value", color="Phase",template="simple_white", labels={
    "Value": "National Estimate of Anxiety(in percent)",
    "Time Period Label": "Time Period (2020)"
}, title="Anxiety Over Time")

df_gender = dfa[dfa['Group'] == "By Gender"]

fig3 = px.bar(df_gender, x="Time Period Label", y="Value", color="Indicator", facet_col="Subgroup", facet_col_wrap=1, labels={
    "Subgroup=Male": "Male",
    "Subgroup=Female": "Female",
    "Value": "Percentage"
}, title="By Gender")

df = pd.read_csv("./national_anxiety.csv")

add_num_list = []
multiply_num_list = []
#---------------------- TEXT ---------------------------- ------------------- DASH ----------------------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, assets_folder='assets')
server = app.server
app.config.suppress_callback_exceptions = True

fig = px.line(df, x="Time_Period", y="Value")

app.layout = html.Div(children=[
    dcc.Graph(
        id='example-graph-1',
        figure=fig1
    ),
    dcc.Graph(
        id='example-graph-2',
        figure=fig2
    ),
    dcc.Graph(
        id='example-graph-3',
        figure=fig3
    ),

    dcc.Graph(
        id='example-graph-4',
        figure=age_fig_1
    ),

    dcc.Graph(
        id='example-graph-5',
        figure=age_fig_12
    )
])



# -------------------------- MAIN ---------------------------- #


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8080, debug=True)

