#Import all packages
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import datetime


#Start the app
app = dash.Dash()

#Format the font and background
colors = {
    'background': '#CBC3E3',
    'font':'Verdana',
    'text': 'black'
}

#App layout using four DIV
app.layout = html.Div([
    html.H1(
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
    html.Div(id='instr-div', children='Enter a number ranging from 0-1000',
    style={
            'textAlign': 'center',
            
            'color': colors['text']
        }),
    dcc.Input(id='my-id', value='', type='text',style={'marginRight':'10px','width':'150px','height':'30px'}),
    html.Div(id='my-div', style={'height':'30px'})
    
],style={'textAlign': 'center','backgroundColor': colors['background']},
)

#The input and output call back that controls the interactive aspect of the program
@app.callback(
    Output(component_id='my-div', component_property='children'),
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
    return ('The all-important value driving our business decisions is: "{}"'.format(arith))
    

#Run the app
if __name__ == '__main__':
    app.run_server()





    