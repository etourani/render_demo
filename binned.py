import numpy as np
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

d0_first_rows = pd.read_csv('./d0_dxdydz.csv')

df_vx = pd.read_csv('./filtered_vx_13e6to17e6.csv')
df_vy = pd.read_csv('./filtered_vy_13e6to17e6.csv')
df_syy = pd.read_csv('./filtered_syy_13e6to17e6.csv')
df_ent = pd.read_csv('./filtered_ent_13e6to17e6.csv')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1("Interactive 3D plots for De = 9 during the extension: velocity (Vx, Vy), Stress (Syy), and crystal clusters", 
                style={'color': '#2C3E50', 'textAlign': 'center', 'backgroundColor': '#AED6F1', 'padding': '10px', 'borderRadius': '5px'}),
        
        html.P("To update the visualization, please control the time slider (min = 2.25 and max = 3 in Hencky strain, in which nucleation seems to be appeared):", 
               style={'color': '#34495E', 'textAlign': 'center'}),
        
        dcc.Slider(
            id='time-slider',
            min=1,
            max=89,
            step=1,
            value=1,
            marks={i: str(i) for i in range(0, 89, 10)},
            updatemode='drag'
        ),
    ], style={'textAlign': 'center', 'padding': '15px'}),
    
    html.Div([
        dcc.Graph(id='vx-plot', style={'width': '49%', 'display': 'inline-block'}),
        dcc.Graph(id='vy-plot', style={'width': '49%', 'display': 'inline-block'}),
        dcc.Graph(id='syy-plot', style={'width': '49%', 'display': 'inline-block'}),
        dcc.Graph(id='ent-plot', style={'width': '49%', 'display': 'inline-block'}),
    ]),
    
    html.Div([
        html.P("Some notes: De and Hencky strain is reported with the relaxation time for C1000 sys (will be corrected later)", 
               style={'padding': '4px'}),
        
        dcc.Textarea(
            id='notes',
            placeholder='Enter your notes here...',
            style={'width': '100%', 'height': '100px'}
        ),
    ], style={'padding': '10px'})
], style={'padding': '10px', 'backgroundColor': '#ECF0F1'})



@app.callback(
    [Output('vx-plot', 'figure'),
     Output('vy-plot', 'figure'),
     Output('syy-plot', 'figure'),
     Output('ent-plot', 'figure')],
    [Input('time-slider', 'value')]
)
def update_plots(step):
    def create_3d_scatter(data, col):
        d_step = d0_first_rows[d0_first_rows['step'] == step]
        x_dim = d_step['xhi'].iloc[0] - d_step['xlo'].iloc[0]
        y_dim = d_step['yhi'].iloc[0] - d_step['ylo'].iloc[0]
        z_dim = d_step['zhi'].iloc[0] - d_step['zlo'].iloc[0]
        
        fig = px.scatter_3d(data, x='xi', y='yi', z='zi', color=col,
                            color_continuous_scale='viridis', opacity=0.5,
                            title=f"{col} for Step: {step}")
        
        camera = dict(
            up=dict(x=0, y=1, z=0),
            center=dict(x=0, y=0, z=0),
            eye=dict(x=0, y=5, z=250)
        )
        
        fig.update_traces(marker=dict(size=3.5, opacity=0.35))
        fig.update_layout(scene_camera=camera, 
                          scene=dict(
                              aspectmode='manual',
                              aspectratio=dict(x=x_dim/2., y=y_dim/2., z=z_dim/1.)
                          ))
        return fig

    vx_data = df_vx[df_vx['step'] == step]
    vy_data = df_vy[df_vy['step'] == step]
    syy_data = df_syy[df_syy['step'] == step]
    ent_data = df_ent[df_ent['step'] == step]

    return create_3d_scatter(vx_data, 'Vx'), create_3d_scatter(vy_data, 'Vy'), create_3d_scatter(syy_data, 'Syy'), create_3d_scatter(ent_data, 'S')

if __name__ == '__main__':
    app.run_server(debug=True)

