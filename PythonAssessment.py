import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import datetime

app = dash.Dash()


colors = {
    'background': '#CBC3E3',
    'font':'Verdana',
    'text': 'black'
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}


app.layout=html.Div([html.H1(
            children='Python Specialist Assessment',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ), 
       html.Div(
        children='A web application to support business decisions.',
        style={
            'textAlign': 'center',
            'height':'70px',
            'color': colors['text']
        }
    ),
     dcc.Tabs([
        dcc.Tab(label='Section One', children=[
            html.Div(id='instr-div', children='Enter a number ranging from 0-1000',
                style={
                        'textAlign': 'center',
                        
                        'color': colors['text']
                 }),
                dcc.Input(id='my-id',  type='number',style={'marginRight':'10px','width':'150px','height':'30px'}),
               html.Div(id='my-div1', style={'height':'30px'})
        ]), 
        dcc.Tab(label='Section Two', children=[
               html.Div(id='my-div2', style={'height':'30px'})
        ]),
    ])
    
    
    
],style={'textAlign': 'center','backgroundColor': colors['background']},
)


#The input and output call back that controls the interactive aspect of the program
@app.callback(    
    Output(component_id='my-div1', component_property='children'),
    Output(component_id='my-div2', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)


#Build a function to convert to UTC 
def update_output_div(input_value):
    utc_time = datetime.datetime.utcnow() 
    utcx_time=int(utc_time.strftime('%H'))
    input_value = float(input_value)
    arith=utcx_time + (2 * input_value)
    #Check User input
    if (input_value>1000):
        return ("Please enter a range of valid numbers less than 1000")
    return (format(arith),'The all-important value driving our business decisions is: "{}"'.format(arith))





if __name__ == '__main__':
    app.run_server(debug=False, port=8022,use_reloader=False, host='127.0.0.1')