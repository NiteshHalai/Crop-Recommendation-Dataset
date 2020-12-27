#importing the modules
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State


import plotly.graph_objs as go
import pandas as pd
import numpy as np

#Data loading and cleaning
df = pd.read_csv('Crop_recommendation.xls')


#features and targets
features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
target = 'labels'


feature_options = []
for feature in features:
    feature_options.append({'label':str(feature), 'value':feature})
    
crop_options = []
for crop in df['label'].unique() :
    crop_options.append({'label':str(crop), 'value':crop})

#dashboard layout
app = dash.Dash()

app.layout = html.Div([
                        html.Div([
                                    html.Hr(),
                                    html.H1('Crop Recommendation Dataset'),
                                    html.P('The data used for this app is from the following link:'),
                                    html.A('Crop Recommendation Dataset', href='https://www.kaggle.com/atharvaingle/crop-recommendation-dataset')
                                    ]),
                            
                            
                        html.Div([
                                    html.Hr(),
                                    html.H2('Crop wise statistics'),
                                    html.Div('Select the crop type:'),
                                    dcc.Dropdown(id='crop-picker', options=crop_options, value='rice'),
                                    html.Div([
                                             html.P('N (Nitrogen)'),
                                             html.P(id='N (Nitrogen) mean'),
                                             html.P(id='N (Nitrogen) range'),
                                             ]
                                             , style={'display':'inline-block', 'width':'14%'}),
                                    html.Div([
                                             html.P('P (Phosphorus)'),
                                             html.P(id='P (Phosphorus) mean'),
                                             html.P(id='P (Phosphorus) range'),
                                             ]
                                             , style={'display':'inline-block', 'width':'14%'}),
                                    html.Div([
                                             html.P('K (Potassium)'),
                                             html.P(id='K (Potassium) mean'),
                                             html.P(id='K (Potassium) range'),
                                             ]
                                             , style={'display':'inline-block', 'width':'14%'}),
                                    html.Div([
                                             html.P('Temperature'),
                                             html.P(id='Temperature mean'),
                                             html.P(id='Temperature range'),
                                             ]
                                             , style={'display':'inline-block', 'width':'14%'}),
                                    html.Div([
                                             html.P('Humidity'),
                                             html.P(id='Humidity mean'),
                                             html.P(id='Humidity range'),
                                             ]
                                             , style={'display':'inline-block', 'width':'14%'}),
                                    html.Div([
                                             html.P('pH'),
                                             html.P(id='pH mean'),
                                             html.P(id='pH range'),
                                             ]
                                             , style={'display':'inline-block', 'width':'15%'}),
                                    html.Div([
                                             html.P('Rainfall'),
                                             html.P(id='Rainfall mean'),
                                             html.P(id='Rainfall range'),
                                             ]
                                             , style={'display':'inline-block', 'width':'15%'}),
                                    ]),
                            
                        html.Div([
                                    html.Hr(),
                                    html.H2('Violin plots'),
                                    dcc.Dropdown(id='feature-picker', options=feature_options, value='N'),
                                    dcc.Graph(id='violin_plot'),
                                    ]),
                            
                        html.Div([
                                    html.Hr(),
                                    html.Div('Developed by Nitesh Halai.'),
                                    html.Div('Mobile/Whatsapp: +254 715 977 346'),
                                    html.Div('Email: nitesh.dataviz@gmail.com'),                    
                                    ]),
                        ])


#Nitrogen mean
@app.callback(Output('N (Nitrogen) mean', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_N_mean(selected_crop):
    mean = round(df[df['label'] == selected_crop]['N'].mean(),2)
    return 'Mean: '+str(mean)


#Nitrogen range
@app.callback(Output('N (Nitrogen) range', 'children'),
              [Input('crop-picker', 'value')]
    )


def update_N_range(selected_crop):
    minimum = round(df[df['label'] == selected_crop]['N'].min(),2)
    maximum = round(df[df['label'] == selected_crop]['N'].max(),2)
    return 'Range: '+str(minimum)+' - '+str(maximum)

#Phosphorus mean
@app.callback(Output('P (Phosphorus) mean', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_P_mean(selected_crop):
    mean = round(df[df['label'] == selected_crop]['P'].mean(),2)
    return 'Mean: '+str(mean)

#Phosphorus range
@app.callback(Output('P (Phosphorus) range', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_P_range(selected_crop):
    minimum = round(df[df['label'] == selected_crop]['P'].min(),2)
    maximum = round(df[df['label'] == selected_crop]['P'].max(),2)
    return 'Range: '+str(minimum)+' - '+str(maximum)


#Potassium mean
@app.callback(Output('K (Potassium) mean', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_K_mean(selected_crop):
    mean = round(df[df['label'] == selected_crop]['K'].mean(),2)
    return 'Mean: '+str(mean)

#Potassium range
@app.callback(Output('K (Potassium) range', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_K_range(selected_crop):
    minimum = round(df[df['label'] == selected_crop]['K'].min(),2)
    maximum = round(df[df['label'] == selected_crop]['K'].max(),2)
    return 'Range: '+str(minimum)+' - '+str(maximum)


#Temperature mean
@app.callback(Output('Temperature mean', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_temperature_mean(selected_crop):
    mean = round(df[df['label'] == selected_crop]['temperature'].mean(),2)
    return 'Mean: '+str(mean)

#Temperature range
@app.callback(Output('Temperature range', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_temperature_range(selected_crop):
    minimum = round(df[df['label'] == selected_crop]['temperature'].min(),2)
    maximum = round(df[df['label'] == selected_crop]['temperature'].max(),2)
    return 'Range: '+str(minimum)+' - '+str(maximum)


#Humidity mean
@app.callback(Output('Humidity mean', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_humidity_mean(selected_crop):
    mean = round(df[df['label'] == selected_crop]['humidity'].mean(),2)
    return 'Mean: '+str(mean)


#Humidity range
@app.callback(Output('Humidity range', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_humidity_range(selected_crop):
    minimum = round(df[df['label'] == selected_crop]['humidity'].min(),2)
    maximum = round(df[df['label'] == selected_crop]['humidity'].max(),2)
    return 'Range: '+str(minimum)+' - '+str(maximum)

#pH mean
@app.callback(Output('pH mean', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_ph_mean(selected_crop):
    mean = round(df[df['label'] == selected_crop]['ph'].mean(),2)
    return 'Mean: '+str(mean)

#pH mean
@app.callback(Output('pH range', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_ph_range(selected_crop):
    minimum = round(df[df['label'] == selected_crop]['ph'].min(),2)
    maximum = round(df[df['label'] == selected_crop]['ph'].max(),2)
    return 'Range: '+str(minimum)+' - '+str(maximum)


#Rainfall mean
@app.callback(Output('Rainfall mean', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_rainfall_mean(selected_crop):
    mean = round(df[df['label'] == selected_crop]['rainfall'].mean(),2)
    return 'Mean: '+str(mean)


#Rainfall range
@app.callback(Output('Rainfall range', 'children'),
              [Input('crop-picker', 'value')]
    )

def update_rainfall_range(selected_crop):
    minimum = round(df[df['label'] == selected_crop]['rainfall'].min(),2)
    maximum = round(df[df['label'] == selected_crop]['rainfall'].max(),2)
    return 'Range: '+str(minimum)+' - '+str(maximum)

#Violin plot
@app.callback(Output('violin_plot', 'figure'),
              [Input('feature-picker','value')]
              )

def update_violin_plot(selected_feature):
    
    violin_plot = go.Violin(
                    x = df['label'],
                    y = df[selected_feature],
                    name='violin plot')

    data1 = [violin_plot]
    
    layout1 = go.Layout(title=selected_feature,
                      xaxis = dict(title='Crop'),
                      yaxis = dict(title=selected_feature))
    
    return {'data':data1,'layout':layout1}    

    

if __name__ == '__main__':
    app.run_server()